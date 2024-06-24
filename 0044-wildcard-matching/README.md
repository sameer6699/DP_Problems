<h2><a href="https://leetcode.com/problems/wildcard-matching">44. Wildcard Matching</a></h2><h3>Hard</h3><hr><p>Given an input string (<code>s</code>) and a pattern (<code>p</code>), implement wildcard pattern matching with support for <code>&#39;?&#39;</code> and <code>&#39;*&#39;</code> where:</p>

<ul>
	<li><code>&#39;?&#39;</code> Matches any single character.</li>
	<li><code>&#39;*&#39;</code> Matches any sequence of characters (including the empty sequence).</li>
</ul>

<p>The matching should cover the <strong>entire</strong> input string (not partial).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aa&quot;, p = &quot;a&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> &quot;a&quot; does not match the entire string &quot;aa&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aa&quot;, p = &quot;*&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong>&nbsp;&#39;*&#39; matches any sequence.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;cb&quot;, p = &quot;?a&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong>&nbsp;&#39;?&#39; matches &#39;c&#39;, but the second letter is &#39;a&#39;, which does not match &#39;b&#39;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length, p.length &lt;= 2000</code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
	<li><code>p</code> contains only lowercase English letters, <code>&#39;?&#39;</code> or <code>&#39;*&#39;</code>.</li>
</ul>

<h1> Solution </h1>
<p>To solve the wildcard matching problem with support for <code>'?'</code> and <code>'*',</code> we can use dynamic programming. The idea is to maintain a 2D DP table where <code>dp[i][j]</code> represents if the first <code>i</code> characters in the string <code> s </code> can match the first<code> j</code> characters of the pattern p.</p>

<ul> <h1>Explnation</h1>
	<li><b>DP Table Initialization:</b> <p><code>dp[0][0]</code> is True because an empty pattern matches an empty string.
<code> dp[0][j] </code> is True if the pattern <code> p </code> up to <code> j </code> characters consists only of <code> '*'</code> because <code> '*'</code> can match an empty sequence.
<code> dp[i][0] </code> is False for <code> i > 0 </code> because a non-empty string cannot match an empty pattern.</p></li>
	<li><b>DP table Update:</b> <p><code>If p[j-1] is '*', it can match zero characters (dp[i][j-1]) or one or more characters (dp[i-1][j]).
If p[j-1] is ? or s[i-1] equals p[j-1], dp[i][j] is True if dp[i-1][j-1] is True.</code></p></li>
	<li></li>
</ul>
