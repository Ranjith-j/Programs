#include<stdio.h>
#include<stdlib.h>
int main()
{
	int n,i,j;
	scanf("%d",&n);
	int mat[n][n];
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			scanf("%d",&mat[i][j]);
		}
	}
	int h,r=0,c=0;
	char str[20];
	scanf("%d",&h);
	for(i=0;i<h;i++)
	{
		scanf("%s",str);
		if(strcmp("right",str)==0 || strcmp("RIGHT",str)==0)
		c++;
		else if(strcmp("left",str)==0 || strcmp("LEFT",str)==0)
		c--;
		else if(strcmp("down",str)==0 || strcmp("DOWN",str)==0)
		r++;
		else if(strcmp("up",str)==0 || strcmp("UP",str)==0)
		r--;	
	}
	printf("%d",mat[r][c]);
}
