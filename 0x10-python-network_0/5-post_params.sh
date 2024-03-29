#!/bin/bash
# Display a Body respond bby sending POST.
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "${1}"
