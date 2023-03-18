class BrowserHistory{
  start: string;
  backwardStack: Array<string>;
  forwardStack: Array<string>;
  constructor(homepage: string){
    this.start = homepage;
    this.backwardStack = [];
    this.forwardStack = [];
  }
  
  visit(url: string): null{
    this.forwardStack = []
    this.backwardStack.push(url)
    return null;
  }
  
  back(steps: number): string{
    if(this.backwardStack.length === 0) return this.start
    const start = this.backwardStack.length - steps > 0 ? this.backwardStack.length - steps : 0;
    const temp = this.backwardStack.splice(start, this.backwardStack.length)
    this.forwardStack = temp.concat(this.forwardStack);
    return this.backwardStack[this.backwardStack.length-1] ?? this.start
  }
  
  forward(steps: number): string{
    const temp = this.forwardStack.splice(0, steps)
    this.backwardStack = this.backwardStack.concat(temp);
    return this.backwardStack[this.backwardStack.length-1] ?? this.start
  }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * var obj = new BrowserHistory(homepage)
 * obj.visit(url)
 * var param_2 = obj.back(steps)
 * var param_3 = obj.forward(steps)
 */