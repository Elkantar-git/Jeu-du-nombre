#! /bin/bash

function Test {
  local testcase="$1"
  local rand_nbr="$2"
  local input="$3"

  echo -e "$input" | TEST_RAND_NBR=$rand_nbr python3 main.py | grep -v "Voulez-vous continuer ?" > .output.txt
  diff .output.txt "./tests/testcases/$testcase.txt"
}

Test test1 42 "50\n30\n0\n100\n42\nn\n"
Test test2 13 "13\n"
