#!/usr/bin/env bash

TOTAL=300      # total number of problems
GROUP=5        # break every GROUP problems
ROW=20         # problems per row
solved=0

printf "\n"

for ((n=1; n<=TOTAL; n++)); do
  # Row header
  if (( (n-1) % ROW == 0 )); then
    row_end=$(( n + ROW - 1 ))
    (( row_end > TOTAL )) && row_end=$TOTAL
    printf "%03d-%03d | " "$n" "$row_end"
  fi

  file=$(printf "%03d" "$n")

  if compgen -G "${file}"'*.py' > /dev/null; then
    printf "✓ "
    ((solved++))
  else
    printf "· "
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

unsolved=$((TOTAL - solved))
percent=$(( solved * 100 / TOTAL ))

printf "\nTotal: %d | Solved: %d | Remaining: %d | %d%% complete\n\n" \
  "$TOTAL" "$solved" "$unsolved" "$percent"

