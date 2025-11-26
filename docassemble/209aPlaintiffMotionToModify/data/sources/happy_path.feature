Feature: Happy paths (no user errors)

- [x] User wants to modify their order
- [x] User uses maximum chars on each page where a description is needed
- [ ] User wants to terminate their order

@generated @slow @modify_max
Scenario: User requests changes using max chars
  Given I start the interview at "209a_plaintiff_s_motion_to_modify"
  Then I get to the question id "download form" with this data:
  | var | value | trigger |
  | a_plaintiff_s_motion_to_modify_qc_v20009_intro | True |  |
  | a_plaintiff_s_motion_to_modify_qc_v20009_preview_question | True |  |
  | acknowledged_information_use | True | |
  | docket_number | 123456789 |  |
  | is_plaintiff['I am the plaintiff'] | True |  |
  | order_type | modify |  |
  | other_parties[0].name.first | Drew |  |
  | other_parties[0].name.last | Defo |  |
  | reason | Because. Green tea jalapeño sesame soba noodles Bulgarian carrot kale lime mango crisp almonds red pepper tempeh vegan pine nuts Italian linguine puttanesca soba noodles asian pear picnic ginger tofu dill.\n\nDessert figs lemon tahini dressing banh mi salad rolls salty green papaya salad macadamia nut cookies mint lime taco bites Thai super chili. Mocha chocolate potato green onions summer fruit salad cremini mushrooms elderberry red lentil curry cool refreshing cucumber splash spring balsamic vinaigrette summer double dark chocolate Thai basil. |  |
  | signature_choice | this_device |  |
  | trial_court | all_courts[0] |  |
  | understand_yes['Yes'] | True |  |
  | users[0].name.first | Uli |  |
  | users[0].name.last | Ulin |  |
  | users[0].signature |  | users[0].signature |
  | users[i].states_above_true['states_true'] | True | users[0].states_above_true |
  | what_to_modify | Visiting hours. Lemonade zest peanut butter bento box lavender lemonade hearty lemon lime minty soy milk vine tomatoes main course ultra creamy avocado pesto samosa coriander chai tea green grapes toasted hazelnuts walnut mushroom tart edamame. Soup simmer peaches blueberry chia seed jam basil paprika chickpea crust pizza blueberry pops edamame hummus Malaysian apple vinaigrette chia seeds cinnamon spiced peppermint blast creamy cauliflower alfredo Thai dragon pepper thyme broccoli. Thai salad. Mediterranean luxury bowl golden banana. |  |
