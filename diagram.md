%%{init: {"flowchart": {"htmlLabels": false}} }%%
flowchart TD
	id00{index.html} -..- id000[What is the reference angle?]
	subgraph app.py
	id00{index.html} -.->|Input One of 30 or 45 or 60| id0{page.html} --- id2[Input Length box]
	id0{page.html} -->|Angle Value| id1[Check Value to Users]
	id0{page.html} ======>|Angle Value| id3[(Calculator)]
	id2[Input Length box] ====>|Length| id3[(Calculator)]
	id2[Input Length box] ------|If Users input the length of side| id6[Show Buttons of base, hypotenuse, height]
	id2[Input Length box] -->|Length| id4[Check Value to Users]
	id4[Check Value to Users] ~~~|If users input Invalid value| id5[hide Buttons of base, hypotenuse, height]
	id6[Show Buttons of base, hypotenuse, height] ====>|Value of the location of the side| id3[(Calculator)]
id3[(Calculator)]==>|Result of the calculation|print
end
	
