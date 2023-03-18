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
    let step: number = steps;
    if(this.backwardStack.length === 0) return this.start
    while(step > 0 && this.backwardStack.length > 0){
      this.forwardStack.push(this.backwardStack.pop())
      step -= 1
    }
    return this.backwardStack[this.backwardStack.length-1] ?? this.start
  }
  
  forward(steps: number): string{
    let step: number = steps;
    while (step > 0 && this.forwardStack.length > 0){
      this.backwardStack.push(this.forwardStack.pop())
      step -= 1
    }
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