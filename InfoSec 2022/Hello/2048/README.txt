For this problem, it brings you to the website: https://infosec-2048.chals.io/

After playing the game, I inspected element and I see on the network tab, it sent a GET request with URL: https://infosec-2048.chals.io/score.php?score=1560

By modifying the score to 2048, it said "Cool score! But you can go higher!"

So I modified score=100000000000 in the URL and it returned the flag:

flag{Y0R_D4_B35T_1N_GAM35}