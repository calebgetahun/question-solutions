from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj = defaultdict(list)
        email_names = dict()

        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                email_names[account[i]] = name
                if account[i] not in adj:
                    adj[account[i]] = []
                for j in range(i+1, len(account)):
                    adj[account[i]].append(account[j])
                    adj[account[j]].append(account[i])

        def dfs(email, visited, curr_comp):
            if email in visited:
                return
            
            visited.add(email)
            curr_comp.append(email)

            for other_email in adj[email]:
                dfs(other_email, visited, curr_comp)
        
        visited = set()
        merged_accounts = []

        for email in adj:
            if email not in visited:
                curr_component = []
                dfs(email, visited, curr_component)
                curr_acc = [email_names[curr_component[0]]]
                curr_component.sort()
                curr_acc.extend(curr_component)
                merged_accounts.append(curr_acc)

        return merged_accounts
    
if __name__ == "__main__":
    sol = Solution()
    accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    print(sol.accountsMerge(accounts))

# TC: O(NKlogNK), where N = number of accounts and K = the maximum amount of emails per account. This is due to the sorting of the emails at the end of our searching when adding to our merged array
# SC: O(NK), since we are storing an adjacency list that contains every single email present which is N*K in the worst case