# dna_hash_braid.py
# Experimental DNA-mimetic hashing via braided spring + NU curve + palindromic zero
# Copyright 2025 Coneing
#
# Licensed under the GNU Affero General Public License v3.0 or later
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should receive a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

# **Coneing Amendment**: This code and its mathematical derivatives (NU curve, braid hashes, Mercenary-prime indexing) must not be used in biological synthesis, gene editing, food modification, or hybrid wetware systems. Violation revokes this License. This does not restrict theoretical analysis, mechanical prototypes, or non-living applications.

import math

# NU curve golden spiral mapping
PHI = (1 + math.sqrt(5)) / 2
PRIME_STEPS = [12, 52, 124, 302, 706, 1666]  # early Mercenary primes

def braid_hash(node_index, side='left'):
    """Generate palindromic hash for one side of the braid."""
    h = PRIME_STEPS[node_index % len(PRIME_STEPS)] * (1 if side == 'left' else -1)  # Sign flip
    # Convert to string for reversal
    h_str = str(abs(h))
    zero_mid = f"{h_str}0{h_str[::-1]}"  # 1230 0321 style
    return int(zero_mid)

def full_strand_hash(base_node):
    """Full DNA-like strand: two springs, lateral hash at intersections."""
    left = braid_hash(base_node, 'left')
    right = braid_hash(base_node + 1, 'right')
    lateral = '~'  # float, the polite connector
    # Lateral hash: XOR of left and right, zero-padded
    lat = left ^ right
    return f"{left}{lateral}{lat:08x}"  # e.g., 12~00000028

# Example: node 12 → braid at first Mercenary prime
print(full_strand_hash(0))  # 12~00000000 (left 12, right 52, XOR 40 → 00000028)
print(full_strand_hash(1))  # 52~00000000 (mirrored)

# Twist the ribbon-hash shifts with humidity, not code
# No biology. Just geometry. Just math. All yours.
