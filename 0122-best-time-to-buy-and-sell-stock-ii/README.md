<h2><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii">122. Best Time to Buy and Sell Stock II</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>

<p> Each day, you may decide to buy and/or sell the stock. You can only hold <strong>at most one</strong> share of the stock at any time. However, you can buy it and then immediately sell it on the <strong>same day</strong>.</p>

<p>Find and return <em>the <strong>maximum</strong> profit you can achieve</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> prices = [7,1,5,3,6,4]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> prices = [1,2,3,4,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> prices = [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= prices[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<h1>Solution</h1>
<p>To solve the problem of finding the best time to buy and sell stocks to maximize profit, you can use a greedy approach. The idea is to sum up all the positive differences between consecutive days' prices because every positive difference represents a profitable transaction.</p>

<h1>Explnation</h1>
<p>
	<ul>
		<li>Iterate through the list of prices from the second day to the last day.</li>
		<li>For each day, if the current day's price is higher than the price of the previous day, it means there's a profit to be made by buying on the previous day and selling on the current day.</li>
		<li> Summarizes all such profits to get the maximum possible profit.</li>
	</ul>
 <p>This approach ensures that you capture all possible profits by making the best transactions every day.</p>
</p>
<h1>Explanation With Example</h1>
<p>
	<ol>
		<li>For prices = [7,1,5,3,6,4], the maximum profit is 7:</li>
		<ol>
			<li>Buy on day <code>2 (price = 1)</code> and sell on day 3 (price = 5), profit = 4.</li>
			<li>Buy on day <code>4 (price = 3)</code> and sell on day <code>5 (price = 6), profit = 3.</code></li>
			<li>Total profit = 4 + 3 = 7.</li>
		</ol>
		<li>For prices = [1,2,3,4,5], the maximum profit is 4:</li>
		<ol>
			<li>Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 4.</li>
		</ol>
		<ol>
			<li>For prices = [7,6,4,3,1], the maximum profit is 0:</li>
			<ol>
				<li>There are no profitable transactions to be made.</li>
			</ol>
		</ol>
	</ol>
 <p>This algorithm runs in O(n) time complexity, where n is the number of days, making it efficient for the input size constraints given in the problem.</p>
</p>
