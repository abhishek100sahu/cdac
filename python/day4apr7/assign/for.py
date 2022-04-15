s = [1, 2, 3, [4, 5,["run", "start"]]]	
for i in range(len(s)):
	if i == 3:
		for j in range(len(s[i])):
			if j == 2:
				for k in s[i][j]:
					if k == "start":
						print(k[3:])

print(s[3][2][1][3])
