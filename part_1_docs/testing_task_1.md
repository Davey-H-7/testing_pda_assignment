### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

 # semicolon missing from else, should be ==
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   
 # 'dif' is incorrect to define a function, should be 'def' + everything following this line should be indented.
 # variable card does not exist, should be returning card1 if true. Missing comma when defining parameters.
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  

#total should initially be set equal to zero and return statement should be outside the for loop otherwise loop will end after 1st iteration
# return string should be interpolated
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
