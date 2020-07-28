import cv2
from os import system, name
if name == "nt":
	system("cls")
else:
	system("clear")

base = cv2.imread("deathbattle.jpg")

def Edit(pfpn1, pfpn2, text1, text2):
	pfp1 = cv2.imread(pfpn1)
	pfp2 = cv2.imread(pfpn2)

	x_offset1 = 7
	y_offset1 = 65
	base[y_offset1:y_offset1+pfp2.shape[0], x_offset1:x_offset1+pfp2.shape[1]] = pfp2

	x_offset2 = 187
	y_offset2 = 65
	base[y_offset2:y_offset2+pfp1.shape[0], x_offset2:x_offset2+pfp1.shape[1]] = pfp1

	font = cv2.FONT_HERSHEY_SIMPLEX
	org = (7, 213)
	org1 = (187, 213)
	fontScale = 0.5
	color = (0, 0, 0)
	thickness = 1
	image = cv2.putText(base, text1, org, font, fontScale, color, thickness, cv2.LINE_AA) 
	image = cv2.putText(base, text2, org1, font, fontScale, color, thickness, cv2.LINE_AA)

	cv2.imwrite('final.jpg', base)