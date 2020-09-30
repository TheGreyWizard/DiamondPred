# %%
def solution(A):
    # A.sort()
    if max(A)<0: 
        return 1
    for num in range(max(A)):
        if num not in A and num > 0:
             return num
        
#%%
print(solution([-22,-1,1]))
print("rest")
# %%

# %%
