1. Describe the algorithm you will use to find the room. Assume all the
information you have is the one given by the sign; you have no
knowledge of the floor plan [0.5 pts]

ANS: You can use the linear search algorithm, which involves checking each room number sequentially to see if it matches the desired classroom number. This process continues until the target classroom is found

2. How many ”steps” it will take to find room EY128? And what is a “step” in
this case? [0.25 pts]

ANS: A 'step' is defined as the action of checking if the room number matches the desired classroom number, followed by moving to the next room. It would take 15 steps to reach room EY128, starting from EY100 and ending at EY128

3. Is this a best-case scenario, worst-case scenario, or neither? [0.25 pts]

ANS: This scenario is closer to the worst-case scenario because room EY128 is near the end of the range. However, it is not the absolute worst-case scenario, which would involve room EY130.

4. With this particular sign and floor layout, explain what a worst-case or best-
case scenario would look like [0.5 pts]

ANS: The best-case scenario occurs when EY128 is the first room checked, requiring 0 steps. The worst-case scenario happens when starting from either EY100 or EY138 and moving sequentially, taking 15 steps if you check from EY  100 and then move forward. Since the rooms are ordered numerically, a linear search is the default approach. However, memorizing the layout allows for an optimized search using a binary search approach, where the middle room is checked first, reducing the worst-case steps from 15 to about 4-5. Additionally, recognizing key points, such as knowing EY128 is closer to EY138 than EY100, further improves navigation efficiency. 



5. Suppose after a few weeks in the term you memorize the layout of the floor.
How would you improve the algorithm to make it more efficient? [0.5 pts]

ANS: After memorizing the layout, you can directly navigate to the target room without performing a sequential search. Instead of starting at the first room (EY100) and checking each one, you could:

Identify which side of the hallway your target room is located on (based on your memorized floor layout).
Walk directly to the target room without unnecessary intermediate checks.
For example, if you know EY128 is near the far end of the hallway, you would walk straight to that area, bypassing the other rooms entirely. This eliminates redundant steps and reduces the time complexity of finding the room from O(n) linear search  to O(1) direct access.