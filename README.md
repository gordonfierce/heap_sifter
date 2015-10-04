# heapsifter
My own CLI tool for managing things I'll get around to. Opinionated and experimental.

## Philosophy

There will always be many more things that you want to do than you can do, so you have to prioritize. There will be many more things you'll want to keep track of than you can reliably remember, so you'll want to externalize your memory in a way that you can rely on. 

I want to keep all of the things I need to do, the things I want to do, the things I want to research, and the ideas that I've had safely in text. In order to do so at scale, I need a powertool custom-built for the job. 

## The TODO Heap

By putting todo items in a heap, we can make sure that the most important one is at the top, and we can find the next most important one with a minimum of fuss. Sorting your todo list from top to bottom isn't very helpful, because time and effort spent meticulously comparing the least important or urgent things you have to do isn't very well spent.

## Usage

Running the base heapsifter command will show the help for the other commands.

`$ heapsifter` 

If you already have a todo.txt file that you haven't converted into a heap, you can do so by invoking

`$ heapsifter heap_it`

If you already have a heaped todo list, then you can add a task to the heap with

`$ heapsifter add`

If you want to see your five most important todo items, run 

`$ heapsifter head`

If you want to remove multiple items from your todo list and maintain the heap invariant, run 

`$ heapsifter batch_remove`

If you want to view, mark done, or repush your top item, run

`$ heapsifter pop`
