"""Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
 You are given n scores.
Store them in a list and find the score of the runner-up.
Input Format
The first line contains n. The second line contains an array All of n integers each separated by a space.
Constraints
• 2 < n ≤ 10
・-100 < Al ≤ 100
Output Format
Print the runner-up score."""
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    unique_scores = sorted(set(arr), reverse=True)
    
    # The second element in the sorted list will be the runner-up score
    runner_up_score = unique_scores[1]
    print( runner_up_score)