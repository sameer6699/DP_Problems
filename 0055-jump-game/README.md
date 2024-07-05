<h2><a href="https://leetcode.com/problems/jump-game">55. Jump Game</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>nums</code>. You are initially positioned at the array&#39;s <strong>first index</strong>, and each element in the array represents your maximum jump length at that position.</p>

<p>Return <code>true</code><em> if you can reach the last index, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,1,1,4]
<strong>Output:</strong> true
<strong>Explanation:</strong> Jump 1 step from index 0 to 1, then 3 steps to the last index.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,1,0,4]
<strong>Output:</strong> false
<strong>Explanation:</strong> You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>
<h1>Solution</h1>
<p> To solve the problem of determining whether you can reach the last index of the array given the maximum jump lengths at each position, you can use a greedy approach. The idea is to keep track of the farthest index you can reach and update this as you iterate through the array. If you can reach or exceed the last index, return true; otherwise, return false.</p>

<h1>Explanation</h1>
<ul>
	<li>Initialize max_reachable to 0, which keeps track of the farthest index that can be reached.</li>
	<li>Iterate through each index i of the array:
	<ol>
		<li>If i is greater than max_reachable, it means the current index is not reachable, so return false.</li>
		<li>Otherwise, update max_reachable to the maximum of its current value and I + nums[i], representing the farthest index that can be reached from the current index.</li>
	</ol>
	</li>
	<li>After the loop, check if max_reachable is at least the last index of the array (len(nums) - 1). If it is, return true; otherwise, return false.</li>
</ul>

