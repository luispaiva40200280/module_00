
def ft_ancient_text(file_name: str) -> str:
    try:
        file = open(file_name, "r")
        content = file.read()
        file.close()
        return content
    except FileNotFoundError:
        return "ERROR: Storage vault not found. Run data generator first"


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    file_name = "ancient_frament.txt"
    content = ft_ancient_text(file_name)
    print(f"Accessing Storage Vault: {file_name}")
    if content.startswith("ERROR: "):
        print()
        print(content)
    else:
        print("Connection established...")
        print()
        print(content)
        print()
        print("Data recovery complete. Storage unit disconnected.")
