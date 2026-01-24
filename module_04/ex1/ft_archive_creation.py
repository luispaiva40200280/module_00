
def ft_archive_creation(file_name: str) -> None:
    if file_name == "new_discovery.txt":
        file = open(file_name, "w", encoding="utf-8")
        file.write("[ENTRY 001] New quantum algorithm discovered\n")
        file.write("[ENTRY 002] Efficiency increased by 347%\n")
        file.write("[ENTRY 003] Archived by Data Archivist trainee\n")
        file.close()


if __name__ == "__main__":
    file_name = "new_discovery.txt"
    if file_name == "new_discovery.txt":
        ft_archive_creation("new_discovery.txt")
        print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
        print(f"\nInitializing new storage unit: {file_name}")
        print("Storage unit created successfully...")
        print("\nInscribing preservation data...")
        print("[ENTRY 001] New quantum algorithm discovered\n" +
              "[ENTRY 002] Efficiency increased by 347%\n" +
              "[ENTRY 003] Archived by Data Archivist trainee\n")
        print("Data inscription complete. Storage unit sealed.")
        print(f"Archive '{file_name}' ready for long-term preservation.")
