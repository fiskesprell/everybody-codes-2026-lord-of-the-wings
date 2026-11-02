#include <stdio.h>
#include <math.h>

int main(void)
{
	double inputArray[] = 
	{
		1,2,3,4,5,6,7,8,9,10,11,12,14,16,17,20,24,29,30,32,34,35,39,40,42,43,48,50,51,52,59,60,62,63,67,68,69,70,74,75,76,78,80,83,84,89,90,92,99,100,106,139,196,198,221,224,255,268,274,275,295,296,334,347,366,370,375,378,388,391,400,449,454,466,475,483,518,538,539,566,567,572,583,641,643,647,686,742,762,830,846,871,876,916,922,938,959,977,980,986

	};
		
	int inputLength = sizeof(inputArray)/sizeof(inputArray[0]);
	double pineConesNeeded = 0;

	for (int i = 0; i < inputLength; i++)
	{
		double currentNum = inputArray[i];
		double squareRoot = sqrt(currentNum);

		if (squareRoot != floor(squareRoot))
		{
			double squareRootRoundedUp = ceil(squareRoot);
			pineConesNeeded += (squareRootRoundedUp * squareRootRoundedUp) - currentNum;
		};
	};
	
	printf("Final Result: %.0f", pineConesNeeded);

	return 0;
}
