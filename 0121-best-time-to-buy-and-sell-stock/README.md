<h2><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock">121. Best Time to Buy and Sell Stock</a></h2><h3>Easy</h3><hr><p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>

<p>You want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.</p>

<p>Return <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> prices = [7,1,5,3,6,4]
<strong>Output:</strong> 5
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> prices = [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transactions are done and the max profit = 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= prices[i] &lt;= 10<sup>4</sup></code></li>
</ul>
<h1>Solution</h1>
<p>To solve the problem of finding the best time to buy and sell stock to maximize profit, you can use a single-pass algorithm. The idea is to keep track of the minimum price encountered so far and calculate the maximum profit by comparing the current price with this minimum price.</p>

<h2>Explantion</h2>
<ul>
	<li><h3>Initialization:</h3><code>min_price</code> is initialized to a very high value <code>(float('inf'))</code>.
<code>max_profit</code> is initialized to <code>0</code>.</li>
	<li><h3>Iteration through the prices:</h3>For each price, if it's lower than <code>min_price</code>, update <code>min_price</code>.
Otherwise, calculate the profit by subtracting <code>min_price</code> from the current price. If this profit is higher than <code>max_profit</code>, update <code>max_profit</code>.</li>
	<li><h3>Return the max_profit: </h3> : After iterating through all prices, the max_profit will be the maximum possible profit.</li>
</ul>
<h2>This algorithm ensures that we only pass through the prices list once, achieving a time complexity of <code>O(n)</code> and space complexity of <code>O(1)</code>.</h2>
