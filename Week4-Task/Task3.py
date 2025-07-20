def tower_of_hanoi(n, source, auxiliary, target):
    if n > 0:
        # Move n-1 disks from source to auxiliary peg
        tower_of_hanoi(n-1, source, target, auxiliary)
        
        # Move nth disk from source to target peg
        print(f"Move disk {n} from {source} to {target}")
        
        # Move n-1 disks from auxiliary to target peg
        tower_of_hanoi(n-1, auxiliary, source, target)

# Example usage
n = 3  # Number of disks
tower_of_hanoi(n, 'A', 'B', 'C')  # A: source, B: auxiliary, C: target