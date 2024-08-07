<h2><a href="https://leetcode.com/problems/jump-game-ii">45. Jump Game II</a></h2><h3>Medium</h3><hr><p>You are given a <strong>0-indexed</strong> array of integers <code>nums</code> of length <code>n</code>. You are initially positioned at <code>nums[0]</code>.</p>

<p>Each element <code>nums[i]</code> represents the maximum length of a forward jump from index <code>i</code>. In other words, if you are at <code>nums[i]</code>, you can jump to any <code>nums[i + j]</code> where:</p>

<ul>
	<li><code>0 &lt;= j &lt;= nums[i]</code> and</li>
	<li><code>i + j &lt; n</code></li>
</ul>

<p>Return <em>the minimum number of jumps to reach </em><code>nums[n - 1]</code>. The test cases are generated such that you can reach <code>nums[n - 1]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,1,1,4]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,0,1,4]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
	<li>It&#39;s guaranteed that you can reach <code>nums[n - 1]</code>.</li>
</ul>
<h1>Explanation</h1>
<p>
	<ul>
		<li>Initialization: 
		<ul>
			<li>jumps keeps track of the number of jumps needed.</li>
			<li>current_end marks the farthest point that can be reached with the current number of jumps.</li>
			<li>farthest is the farthest point that can be reached from any index within the current range.</li>
		</ul>
		</li>
		<li> Iteration:
			<ul>
				<li>Iterate through the array (excluding the last element since reaching the last element is the goal).</li>
				<li>For each index, update the farthest to be the maximum of its current value or the farthest point that can be reached from the current index.</li>
				<li>If the current index reaches current_end, we need another jump. Increment jumps and update current_end to farthest.</li>
			</ul>
		</li>
		<li> Break Condition:
			<ul>
				<li>If current_end exceeds or reaches the last index, we break out of the loop.</li>
			</ul>
		</li>
	</ul>
</p>
