from sort import external_sort


def main():
    input_path = 'numbers_1e7.bin'  # путь к исходному файлу
    output_path = 'sorted_numbers.bin'
    M_values = [2 * 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7]

    results = []
    for M in M_values:
        print(f"Запуск M = {M}...")
        stats = external_sort(input_path, output_path, M, verbose=False)
        results.append(stats)
        print(f"M={M}: phase1={stats['phase1_time']:.2f}s, phase2={stats['phase2_time']:.2f}s, "
              f"cmp1={stats['phase1_comparisons']}, cmp2={stats['phase2_comparisons']}, "
              f"total_cmp={stats['total_comparisons']}, chunks={stats['num_chunks']}")

    print("\nM\tphase1_time\tphase2_time\tcmp1\tcmp2\ttotal_cmp\tchunks")
    for s in results:
        print(f"{s['M']}\t{s['phase1_time']:.2f}\t{s['phase2_time']:.2f}\t"
              f"{s['phase1_comparisons']}\t{s['phase2_comparisons']}\t"
              f"{s['total_comparisons']}\t{s['num_chunks']}")


if __name__ == '__main__':
    main()
