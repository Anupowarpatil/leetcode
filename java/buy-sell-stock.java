class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int maxP=0,minP=Integer.MAX_VALUE;
        for(int i=0;i<n;i++)
        {
            if(minP>prices[i])
            {
                minP=prices[i];
            }
            maxP=Math.max(maxP,prices[i]-minP);
        }
        return maxP;
    }
}
