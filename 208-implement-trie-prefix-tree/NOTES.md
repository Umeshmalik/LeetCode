ring isTrieNode will be basicly storing map of max 26 character and flag if any string is getting end over here.
​
in insert no need to make whole new tree, if we are having same string upto any context, we will use existing tree upto that node upto where we string is already stored. and same in reterival and startWith we will go through nodes in their children and check if string is there or not