import os
import sys
import time
import tempfile
import shutil
from array import array
from typing import Optional
from heapsort import heapsort_inplace
from binaryheap import BinaryHeap


def make_counting_comparator(base_cmp, counter):
    def cmp(a, b):
        counter[0] += 1
        return base_cmp(a, b)

    return cmp


def read_chunk(f, count: int, itemsize: int = 4):
    data = f.read(count * itemsize)
    if not data:
        return None
    arr = array('i')
    arr.frombytes(data)
    if sys.byteorder != 'little':
        arr.byteswap()
    return arr


def write_chunk(f, arr: array) -> None:
    if sys.byteorder != 'little':
        arr = array('i', arr)
        arr.byteswap()
    f.write(arr.tobytes())


def external_sort(input_path: str, output_path: str, M: int, temp_dir: Optional[str] = None,
                  verbose: bool = False) -> dict:
    if temp_dir is None:
        temp_dir = tempfile.mkdtemp(prefix='extsort_')
    else:
        os.makedirs(temp_dir, exist_ok=True)

    # ---------- Этап 1: чтение блоками по M, сортировка, запись во временные файлы ----------
    phase1_cmp = [0]
    phase1_time = 0.0
    temp_files = []
    chunk_index = 0
    cmp_max = lambda a, b: a > b

    t0 = time.perf_counter()
    with open(input_path, 'rb') as fin:
        while True:
            arr = read_chunk(fin, M)
            if arr is None or len(arr) == 0:
                break
            heapsort_inplace(arr, cmp_max, phase1_cmp)
            temp_path = os.path.join(temp_dir, f'chunk_{chunk_index}.bin')
            with open(temp_path, 'wb') as fout:
                write_chunk(fout, arr)
            temp_files.append(temp_path)
            chunk_index += 1
    phase1_time = time.perf_counter() - t0

    # ---------- Этап 2: слияние всех временных файлов через min-кучу ----------
    phase2_cmp = [0]
    phase2_time = 0.0
    base_cmp = lambda a, b: a[0] < b[0]
    counting_cmp = make_counting_comparator(base_cmp, phase2_cmp)

    t0 = time.perf_counter()
    files = [open(p, 'rb') for p in temp_files]
    heap = BinaryHeap(comparator=counting_cmp)

    # Загружаем по одному первому числу из каждого файла
    for idx, f in enumerate(files):
        arr = read_chunk(f, 1)
        if arr is not None and len(arr) > 0:
            heap.push((arr[0], idx))
        else:
            f.close()
            files[idx] = None

    with open(output_path, 'wb') as fout:
        while heap:
            val, idx = heap.pop()
            write_chunk(fout, array('i', [val]))
            f = files[idx]
            arr = read_chunk(f, 1)
            if arr is not None and len(arr) > 0:
                heap.push((arr[0], idx))
            else:
                f.close()
                files[idx] = None

    for f in files:
        if f is not None:
            f.close()

    phase2_time = time.perf_counter() - t0

    if verbose:
        print(f"Временные файлы: {temp_dir}")
    else:
        shutil.rmtree(temp_dir, ignore_errors=True)

    return {
        'M': M,
        'phase1_time': phase1_time,
        'phase2_time': phase2_time,
        'phase1_comparisons': phase1_cmp[0],
        'phase2_comparisons': phase2_cmp[0],
        'total_comparisons': phase1_cmp[0] + phase2_cmp[0],
        'num_chunks': chunk_index,
    }
