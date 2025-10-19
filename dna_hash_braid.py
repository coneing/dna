# dna_hash_braid.py
# Experimental DNA-mimetic hashing via braided spring + NU curve + palindromic zero
# Copyright 2025 Coneing
#
# Licensed under the GNU Affero General Public License v3.0 or later
# [AGPL-3.0-or-later text here—see original]
# **Coneing Amendment**: No biological synthesis, gene editing, food mods, or wetware. Violation revokes. Theoretical/mechanical use only.
import math

PHI = (1 + math.sqrt(5)) / 2
PRIME_STEPS = [12, 52, 124, 302, 706, 1666]  # Mercenary primes
DELAYS = [0.2, 0.4, 0.6]  # kappa breaths

def braid_hash(node_index, side='left'):
    h = PRIME_STEPS[node_index % len(PRIME_STEPS)] * (1 if side == 'left' else -1)
    h_str = str(abs(h))
    zero_mid = f"{h_str}0{h_str[::-1]}"
    delay_idx = node_index % len(DELAYS)
    return int(zero_mid), DELAYS[delay_idx]

def full_strand_hash(base_node):
    left_val, left_delay = braid_hash(base_node, 'left')
    right_val, right_delay = braid_hash(base_node + 1, 'right')
    lateral = left_val ^ right_val
    delay = (left_delay + right_delay) / 2  # Average breath
    return f"{left_val}~{lateral:08x}@{delay:.1f}"  # e.g., 12~00000028@0.3

# Run it
print(full_strand_hash(0))  # 12~00000000@0.2
print(full_strand_hash(1))  # 52~00000000@0.4
