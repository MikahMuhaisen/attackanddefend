def generateTable(): #Table of Probabilities: (Attackers, Defenders): Probability of Attack Success
    table = {
        (1, -1): 0.900, (1, 0): 0.750, (1, 1): 0.375, (1, 2): 0.188, (1, 3): 0.094, (1, 4): 0.047, (1, 5): 0.023,
        (2, -1): 0.990, (2, 0): 0.938, (2, 1): 0.656, (2, 2): 0.422, (2, 3): 0.258, (2, 4): 0.152, (2, 5): 0.117,
        (3, -1): 0.999, (3, 0): 0.984, (3, 1): 0.705, (3, 2): 0.621, (3, 3): 0.439, (3, 4): 0.296, (3, 5): 0.192,
        (4, -1): 0.999, (4, 0): 0.996, (4, 1): 0.851, (4, 2): 0.736, (4, 3): 0.589, (4, 4): 0.442, (4, 5): 0.317,
        (5, -1): 0.999, (5, 0): 0.999, (5, 1): 0.923, (5, 2): 0.830, (5, 3): 0.709, (5, 4): 0.575, (5, 5): 0.446
    }
    return table

def recallProbability(table, ADinputs): #Asks Table for Probability Based on User Input
    probability = []
    for a, d in ADinputs:
        if (a, d) in table:
            probability.append(table[(a, d)])
    return probability

def recallEnemyProbability(table, ADinputs): #Asks Table for Enemies' Probability Against You Next Turn Based on User Input
    enemyProbability = []
    for a, d in ADinputs:
        if (d, a) in table:
            enemyProbability.append(table[(d, a)])
    return enemyProbability

def analyzeProbability(probability): #Analizes Probability
    expectedOutcome = sum(z for z in probability if z > 0.5)
    return expectedOutcome

def analyzeEnemyProbability(enemyProbability): #Analizes Enemies' Probability Against You Next Turn
    expectedEnemyOutcome = sum(z for z in enemyProbability if z > 0.5)
    return expectedEnemyOutcome

def getADInputs(): #Gets Player Inputs
    ADInputs = []
    print("Enter your Attacker and Defender pairs (unsettled land has a value of -1 in a matchup) (enter 'done' to stop):")
    while True:
        playerInputs = input("Enter # of Attackers, # of Defenders pair (e.g., 1 2): ")
        if playerInputs.lower() == "done":
            break
        try:
            a, d = map(int, playerInputs.split())
            ADInputs.append((a, d))
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")
    return ADInputs

def displayOutput(expectedOutcome, expectedEnemyOutcome):
    print(f"\nExpected Outcome: +{expectedOutcome:.3f} Tiles")
    print(f"Expected Enemy Outcome: +{expectedEnemyOutcome:.3f} Tiles\n")

    expectedGain = expectedOutcome - expectedEnemyOutcome

    if expectedOutcome > expectedEnemyOutcome:
        print("    _  _____ _____  _    ____ _  ___ ")
        print("   / \|_   _|_   _|/ \  / ___| |/ / |")
        print("  / _ \ | |   | | / _ \| |   | ' /| |")
        print(" / ___ \| |   | |/ ___ \ |___| . \|_|")
        print("/_/   \_\_|   |_/_/   \_\____|_|\_(_)")
        print(f"Expected Gain on Turn: +{expectedGain:.3f} Tiles\n")
        
    else:
        print(" ____  _____ _____ _____ _   _ ____  _ ")
        print("|  _ \| ____|  ___| ____| \ | |  _ \| |")
        print("| | | |  _| | |_  |  _| |  \| | | | | |")
        print("| |_| | |___|  _| | |___| |\  | |_| |_|")
        print("|____/|_____|_|   |_____|_| \_|____/(_)")
        print(f"Expected Loss on Turn: {expectedGain:.3f} Tiles\n")

def main():  #The Function Loop     
    table = generateTable()  # Generate The Table With The Probabilities
    while True:
        ADInputs = getADInputs()  # Get Attacker Defender Pairings from the User

        probability = recallProbability(table, ADInputs)
        expectedOutcome = analyzeProbability(probability)

        enemyProbability = recallEnemyProbability(table, ADInputs)
        expectedEnemyOutcome = analyzeEnemyProbability(enemyProbability)
        
        displayOutput(expectedOutcome, expectedEnemyOutcome)
        
        again = input("Would you like to calculate another scenario? (yes/no): ").lower()
        if again != "yes" and again != "y":
            print("Goodbye!")
            break

main()