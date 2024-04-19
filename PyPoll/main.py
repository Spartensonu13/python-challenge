import os
import csv

# intialize variables
totalVotes = 0
candidateList = []
candidateTotalVotes = []

# path to connect data from election_data.csv
electionData = os.path.join("Pypoll","Resources", "election_data.csv")

# path to analysis file
analysisFilePath = os.path.join("PyPoll", "analysis", "analysis.txt")

# open csv file
with open(electionData) as electionDataCsvFile: 
    # read csv file
    electionDataReader = csv.reader(electionDataCsvFile, delimiter= ',')

    # skip header row
    next(electionDataReader)

    # loop throgh each csv file
    for row in electionDataReader:

        # calculate total votes
        totalVotes = totalVotes + 1
        
        # get distinct candidate names and candidate total votes
        if candidateList.count(row[2]) == 0 :
            candidateList.append(row[2])
            candidateTotalVotes.append(1)
        else:
            candidateIndex = candidateList.index(row[2])
            candidateTotalVotes[candidateIndex] = candidateTotalVotes[candidateIndex] + 1   

# create and write to analysis file
with open(analysisFilePath, 'w') as analysisFile:

    # write total votes to file
    analysisFile.write("Election Results")
    analysisFile.write("\n-------------------------")
    analysisFile.write(f"\nTotal Votes: {totalVotes}")
    analysisFile.write("\n-------------------------")

    for i in range(len(candidateList)):
        # calculate vote percentage for each candidate
        votePercentage = (candidateTotalVotes[i]/totalVotes) * 100

        # write candidate name, vote percentage, total votes
        analysisFile.write(f"\n {candidateList[i]}: ")
        analysisFile.write(f" {votePercentage:.3f}%")
        analysisFile.write(f" ({candidateTotalVotes[i]})")

    # get winner index
    winnerIndex = candidateTotalVotes.index(max(candidateTotalVotes))

    # write winner name to analysis file
    analysisFile.write("\n-------------------------")
    analysisFile.write(f"\nWinner: {candidateList[winnerIndex]} ")
    analysisFile.write("\n-------------------------")

    # close file
    analysisFile.close

#read and print analysis file
with open(analysisFilePath, 'r') as analysisFileReader:
    print(analysisFileReader.read())