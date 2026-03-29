#!/usr/bin/env bash

TOTAL=500      # total number of problems
GROUP=5        # break every GROUP problems
ROW=20         # problems per row

solved=0
skipped=0

skip_problem() {
  local n=$1
  (( (n >= 175 && n <= 178) ||
     (n >= 180 && n <= 185) ||
     (n >= 196 && n <= 197) ||
     n == 262 ))
}

printf "\n"

for ((n=1; n<=TOTAL; n++)); do
  # Row header
  if (( (n-1) % ROW == 0 )); then
    row_end=$(( n + ROW - 1 ))
    (( row_end > TOTAL )) && row_end=$TOTAL
    printf "%03d-%03d | " "$n" "$row_end"
  fi

  if skip_problem "$n"; then
    printf "%s " "-"
    ((skipped++))
  else
    file=$(printf "%03d" "$n")

    if compgen -G "${file}"'*.py' > /dev/null; then
      printf "✓ "
      ((solved++))
    else
      printf "· "
    fi
  fi

  pos=$(( (n-1)%ROW + 1 ))

  # Break every GROUP
  if (( pos % GROUP == 0 && pos != ROW )); then
    printf "| "
  fi

  # End of row
  if (( pos == ROW )); then
    printf "|\n"
  fi
done

# Handle incomplete last row
if (( TOTAL % ROW != 0 )); then
  printf "|\n"
fi

effective_total=$((TOTAL - skipped))
unsolved=$((effective_total - solved))

if (( effective_total > 0 )); then
  percent=$(( solved * 100 / effective_total ))
else
  percent=0
fi

printf "\nTotal: %d | Solved: %d | Remaining: %d | Skipped: %d | %d%% complete\n\n" \
  "$effective_total" "$solved" "$unsolved" "$skipped" "$percent"
