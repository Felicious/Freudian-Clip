# NER Example Python Code Snippet

For the blog post "How Coding and AI Aren't Mutually Exclusive"

To get a better sense of how to preprocessing for Named Entity Recognition (NER) works, try this simple example (:

## I need your input!

Currently, you can test my sentence and corresponding entity labels that's stored in the "sentence.txt" and "entities.txt." files but downloading all three files on my Github to get the same output I showed in my blog post.

But if you'd like to test your own sentence, you can modify my "sentence" file with something of your own. Unfortunately, it can only read one line of text, so if you have multiple sentences, DON'T press enter!

Do

```
I like boba. And cats. But not exercising."
```

Don't

```
I like boba.
And cats.
But not exercising.
```

Additionally, you'll need to modify the "entities.txt" file to label the entities. The way I labeled them was

```
0: unrelated words
B-BEHAVIOR: first word describing a behavior
I-BEHAVIOR: proceeding words describing behavior
```

Therefore, if the sentence "I like drinking boba" is in the "sentence.txt" file, you need to label each word in the "entities.txt" file

```
0 0 B-BEHAVIOR I-BEHAVIOR
```
