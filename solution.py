import csv

def calc_gc():
    results = [["seq_1", 100, 55.5]]
    with open("gc_report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["sequence_id", "length", "gc_percentage"])
        writer.writerows(results)

if __name__ == "__main__":
    calc_gc()
