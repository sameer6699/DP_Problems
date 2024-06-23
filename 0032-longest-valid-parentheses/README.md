<h2><a href="https://leetcode.com/problems/longest-valid-parentheses">32. Longest Valid Parentheses</a></h2><h3>Hard</h3><hr><p>Given a string containing just the characters <code>&#39;(&#39;</code> and <code>&#39;)&#39;</code>, return <em>the length of the longest valid (well-formed) parentheses </em><span data-keyword="substring-nonempty"><em>substring</em></span>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(()&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> The longest valid parentheses substring is &quot;()&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;)()())&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest valid parentheses substring is &quot;()()&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;&quot;
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>s[i]</code> is <code>&#39;(&#39;</code>, or <code>&#39;)&#39;</code>.</li>
</ul>

<h1> Solution </h1>
<p> To solve the problem of finding the longest valid parentheses substring, we can use dynamic programming or a stack-based approach. I'll provide the stack-based approach as it is intuitive and efficient.</p>

<ul> <h1> Stack-Based Approach: </h1>
	<li>Initialization <p>Use a stack to store the indices of the characters.
	Push -1 onto the stack initially to handle the edge case where the valid substring starts from the beginning.</p></li>
	<li>Iterate through the string <p>For each character, if it is <code>'('</code>, push its index onto the stack.
	If it is <code>')'</code>, pop from the stack. If the stack is not empty after popping, calculate the length of the current valid substring using the current index and the index at the top of the stack. Update the maximum length if necessary.
	If the stack is empty after popping, push the current index onto the stack as a new base for the next potential valid substring.
</p></li>
	<li>Result. <p> The maximum length calculated during the iteration will be the length of the longest valid parentheses substring.</p></li>
</ul>
