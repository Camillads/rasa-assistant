#### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## greet + goodbye
* greet: Hi!
  - utter_greet
* bye: Bye
  - utter_bye

## greet + thanks
* greet: Hello there
  - utter_greet
* thank: thanks a bunch
  - utter_noworries

## greet + thanks + goodbye
* greet: Hey
  - utter_greet
* thank: thank you
  - utter_noworries
* bye: bye bye
  - utter_bye