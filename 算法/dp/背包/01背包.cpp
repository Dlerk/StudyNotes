/*

有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。

第 i 件物品的体积是 vi，价值是 wi。

求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出最大价值。

输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品数量和背包容积。

接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 件物品的体积和价值。

输出格式
输出一个整数，表示最大价值。

*/

#include <iostream>
#include <cmath>
using namespace std;

#define N 1001

int n ; 
int V ;
int dp_roll[N] ;
int dp_2d[N][N] ;
int vi[N] , wi[N];

void slove_2d()
{
    /*  
        动态转移方程
        dp[i][j] =  max( dp[i-1][j] , dp[i-1][j-vi[i]]+wi[i] ) 
        dp[i][j]为抉择第i件物品时，在背包空间为j时的局部最优解(价值最大)
    */

    for( int i=1 ; i<=n ; i++ )
        for( int j=0 ; j<=V ; j++ )
        {
            dp_2d[i][j] = dp_2d[i-1][j] ;
            if( j >= vi[i] )
                if( dp_2d[i][j] < (dp_2d[i-1][j-vi[i]]+wi[i]) )
                    dp_2d[i][j] = dp_2d[i-1][j-vi[i]]+wi[i] ;
        }

    cout << dp_2d[n][V] << endl ;
}

void slove_roll()
{
    /*
        滚动数组优化：
        状态转移每次只与上一层有关，所以用一个一维数组就可以
            动态转移方程：
            dp[i] = max( dp[i] , dp[i-v[i]]+w[i] )
            相当于二维中的
            dp[i][j] =  max( dp[i-1][j] , dp[i-1][j-vi[i]]+wi[i] ) 
            因此内层循环需要从大到小循环：这样做的话能保证一定用的是上一层的状态
            若是从小到大循环，则变为 dp[i][j]=max(dp[i][j],dp[i][j-v[i]]+w[i]) 
    */

    for( int i=1 ; i<=n ; i++ )
        for( int j=V ; j>=0 ; j++ )
        {
            if( dp_roll[j] < dp_roll[j-vi[i]]+wi[i] )
                dp_roll[j] = dp_roll[j-vi[i]]+wi[i] ;
        }

    cout << dp_roll[V] << endl ;

}


int main()
{

    cin >> n >> V ;
    for( int i=1 ; i<=n ; i++ )    
        cin >> vi[i] >> wi[i];

    slove_2d() ;
    slove_roll() ;

    return 0;
}
