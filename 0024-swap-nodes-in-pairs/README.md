<h2><a href="https://leetcode.com/problems/swap-nodes-in-pairs">24. Swap Nodes in Pairs</a></h2><h3>Medium</h3><hr>
<p>Given a&nbsp;linked list, swap every two adjacent nodes and return its head. You must solve the problem without&nbsp;modifying the values in the list&#39;s nodes (i.e., only nodes themselves may be changed.)</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg" style="width: 422px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4]
<strong>Output:</strong> [2,1,4,3]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = []
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> head = [1]
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the&nbsp;list&nbsp;is in the range <code>[0, 100]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 100</code></li>
</ul>

<h1> Solution </h1>
<p> To solve the problem of swapping every two adjacent nodes in a linked list, we'll implement a function swap pairs. This function will iteratively swap nodes in pairs without modifying the nodes' values.</p>

<h2> Explnation </h2>

<dl>
<dt>ListNode Class: </dt>
<dd> Defines the structure of a node in the linked list. </dd>
	
<dt> swapPairs Method: </dt>
<dd>- A dummy node is used to simplify the swapping process, especially for the head of the list. </dd>
<dd>- We use a pointer current starting from the dummy node. </dd>
<dd>- We iterate through the list, swapping nodes in pairs </dd>
<dd>- first points to the first node of the pair. </dd>
<dd>- second points to the second node of the pair. </dd>
<dd>- The swap is performed by adjusting the next pointers. </dd>
<dd>- After swapping, we move current to the next pair. </dd>

	
</dl>


