<h2><a href="https://leetcode.com/problems/reverse-nodes-in-k-group">25. Reverse Nodes in k-Group</a></h2><h3>Hard</h3><hr><p>Given the <code>head</code> of a linked list, reverse the nodes of the list <code>k</code> at a time, and return <em>the modified list</em>.</p>

<p><code>k</code> is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of <code>k</code> then left-out nodes, in the end, should remain as it is.</p>

<p>You may not alter the values in the list&#39;s nodes, only nodes themselves may be changed.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5], k = 2
<strong>Output:</strong> [2,1,4,3,5]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5], k = 3
<strong>Output:</strong> [3,2,1,4,5]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is <code>n</code>.</li>
	<li><code>1 &lt;= k &lt;= n &lt;= 5000</code></li>
	<li><code>0 &lt;= Node.val &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow-up:</strong> Can you solve the problem in <code>O(1)</code> extra memory space?</p>

<h1> Solution </h1>
<p> To reverse the nodes of a linked list in groups of k, we can iteratively reverse each group of k nodes while keeping track of the pointers to connect the reversed groups. </p>

<dl> Explanation
<dt> List Node Classes </dt>
<dd>- Defines the structure of a node in the linked list.</dd>
<dt>reverseKGroup Method</dt>
<dd>- <b>reverse_linked_list Function:</b> Reverses k nodes of the linked list starting from a given node.</dd>
<dd>- <b>Length Calculation:</b> First, we calculate the length of the linked list to ensure we only reverse complete groups of k nodes.</dd>
<dd>- <b>Dummy Node:</b> Used to simplify the edge cases and provide a starting point for the reversed list.</dd>
<dd>- <b>Iterative Reversal:</b> We reverse each group of k nodes and connect them correctly.</dd>
<dd>- <b>Connecting Groups:</b> Properly connect the reversed groups with the next part of the list and the previous part.</dd>
</dl>
