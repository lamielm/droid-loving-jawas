# Assignment 4 - Stacks, Queues, and Merge Sort. Project uses Assignment 3 solution.

## Author

Landon Lamie

## Description

The Jawas on Tatooine are pleased with the job you have done on the droid system so far. Since they started using it, they have decided that they would like a few new features added. They would like to be able to sort their list of droids in two different ways. It is your job to create these sorts for them.

They would like to sort the droids by category. If the list is printed after using this sort, the program will display the droids in the following order: (Astromech, Janitor, Utility, Protocol). There does not need to be any order to the droids within those categories. Just all the Astromechs, then all the Janitors, and so on.

They would also like to sort the droids by the Total Cost ranging from the cheapest droid to the most expensive droid.

The menu options and methods that you add should only sort the droid collection. Printing it should still be delegated to the print menu option that already exists. This means that sorting it will overwrite the original order in the list, and that is okay.

Details about how each sort will work are explained below.

You need to add menu options and methods to a finished assignment 3 to complete assignment 4, and add the above mentioned functionality.

Using the assignment link will give you my finished implementation of Assignment 3 as a starting place. If you would rather use your implementation of assignment 3, just delete all of my modules, and add your modules in it's place. (Or replace the code of my classes with the code from your classes). This way you are still working from the repository you get from the assignment list.

You are not required to use your implementation of Assignment 3. In fact, it would be easier for me to grade if you used mine, but you are free to use your own if that is easier for you.

You should add some dummy data to the program to make testing easier. Once the droid collection is instantiated, you should hard code the insertion of some droids into the collection. Do at least 2 of each type of droid for a total of 8, and make sure to add them in an order that is different from the sort results so that you know your sorts work. This will allow both you and I a way to test both sorts without having to use the UI to create droids.

The method by which both of these sorts get done is described below:

### Categorize by model (Modified Bucket sort)
In order to sort the list by category, you will do the following things:

* Create a `Stack` class in a module / file named `datastructures.py`. The implementation should be in the style of a linked list.
* Create a `Queue` class in a module / file named `datastructures.py`. The implementation should be in the style of a linked list.
* Add a method to your droid collection that will do this sort on the collection.
  * In the method, create an instance of the `Stack` class for each type of droid (4 in total)
  * In the method, create a single instance of the `Queue` class (Just 1 of these).
  * Loop through your list of droids, and for each one:
    * Determine what type of droid it is by inspecting the instance type with the `isinstance` method, and then Push the droid onto the appropriate stack. More information about how to inspect the instance type of an object can be found below.
    * Once all of the droids are on the various stacks, start Popping the droids off of the stacks and enqueue them in the Queue. (Make sure you process the stacks in the correct order so that the order of the queue is the order specified above for the sort)
    * Once all of the droids are in the Queue, replace the original list of droids with the droids in the queue by dequeuing a droid one at a time, and placing it back into the original list.

I realize that this above sort could be done without using a queue, but I want you to use a queue in this program. Therefore you have to take from the stack and put into the queue, and then remove from the queue and put into the original list vs going straight from the stacks to the list.

Here is a diagram that attempts to show the general flow of the algorithm. On top is DroidCollection's underlying droid list. The algorithm will then remove each droid from the list and push it on the appropriate stack. One for each droid. That is the vertical parts of the diagram. Then after the stacks are full, they will be popped off and enqueued in the single droid queue. This is the bottom part of the diagram. Lastly, the droids are removed from the queue and put back in the original list at the top.

![Categorize by model diagram](https://barnesbrothers.net/cis226/assignmentImages/cis226_assignment_4_bucket_sort.png)

For this sort, you need to loop through the droids and determine what type of droid the current one is so that you can push it on to the appropriate stack. That work of determining what Type the current instance is can be done a couple of different ways but I am asking you to use the `isinstance` method. Below there is a Geeks for Geeks article that might aid in your work to test what type of a droid a variable contains so that you can push it on to the correct stack:

[Geeks for Geeks](https://www.geeksforgeeks.org/type-isinstance-python/)

<br/><br/><br/><br/><br/><br/>

### Sort by Total Cost using Merge Sort
In order to sort the list by the Total Cost, you will do the following things:

* Implement the required dunder methods in the `Droid` class that will be needed in order to be able to compare one instance of a `Droid` to another in order to know which comes before which. See more info below.
* Create a `MergeSort` class in a module / file named `mergesort.py` with a sort method that takes in a `list`. You should be doing a top-down implementation using a python `list` (NOT linked list), and use an auxiliary python `list` to store temporary information. (My visualization has code that you can reference.)
* Add a method to your droid collection that will send the droid collection's underlying `list` over to the `MergeSort` class's `sort` method to get the list sorted. Since `list` is an object, it will be passed by reference. So, the sort will end up altering the original list. No need to try and pass anything back.
NOTE: If any of this is confusing, be sure to ask about it in class! I DO NOT want you hung up on what you are supposed to do.

For this sort, you have to do a few steps. For starters, I am assuming that you are going to use the MergeSort code from my visualization.

That code tries to compare two droids and determine which one comes before the other. Being able to do that comparison means that the droid classes need to have the correct "Rich Comparison" dunder methods overridden. That way when things like `<`, `<=`, `>`, `>=` are used with instances of a droid on either side, they will do something useful.
If you look at the MergeSort code, you will see that it makes use of `<`. So, at a minimum, that Rich Comparison dunder method needs to be overridden. But, you may choose to do more than that single one as well since only doing one seems a little weird. With that said, I would omit doing the `==` and `!=` ones as two droids with the same price does not mean that they are the same droid.

As for the contents of the methods you need to implement, you should reference the following links. It contains information about those methods. The second one has some examples listed.

[Python Docs - Python Rich Comparison Methods](https://docs.python.org/3/reference/datamodel.html#object.__lt__)

[Porting Guide - Python Rich Comparison Methods](https://portingguide.readthedocs.io/en/latest/comparisons.html)

You are free to do anything above an beyond what is listed here. The only "Requirements" are listed below.

Solution Must:
* Add some hard coded droids to the droid collection.
* Create `Stack` class in `datastructures.py`.
* Create `Queue` class in `datastructures.py`.
* Update `Droid` and override the needed rich comparison dunder methods.
* Create `MergeSort` class in `mergesort.py`.
* Update the program to allow options to sort by Model, or by Total Cost.
* Add methods to the Droid Collection class to do each of the sorts.
* Use the `Stack`, and `Queue` to perform a modified bucket sort to categorize by model.
* Use the `MergeSort` to perform a sort on the TotalCost.

Below is the original Assignment 3 description for reference.

### Notes

Be sure to think about what the time complexity for the bucket sort will be. Think about how it compares to that of a normal sort such as Merge or Bubble. Also consider the space complexity of merge sort compared to that of bubble sort. You may see questions related to this on the next exam.

## Grading
| Feature                                    | Points |
|--------------------------------------------|--------|
| Add Hard Coded Droids                      | 5      |
| Add Stack Class                            | 10     |
| Add Queue Class                            | 10     |
| Droid implements required dunder methods   | 10     |
| Create MergeSort Algorithm                 | 15     |
| Add methods to DroidCollection to do sorts | 5      |
| Sorting By Category Works Correctly        | 15     |
| Sorting By Total Cost Works Correctly      | 15     |
| UI is updated correctly                    | 5      |
| Documentation                              | 5      |
| README                                     | 5      |
| **Total**                                  | **100**|

## Outside Resources Used



## Known Problems, Issues, And/Or Errors in the Program



<br/><br/><br/><br/><br/><br/><br/><br/>

## Assignment 3 - Description for reference

### Description

The Jawas on Tatooine have recently opened a droid factory and they want to hire you to write a program to hold a list of the available droids, and the price of each droid. The price is based on the type: (protocol, utility, janitor, or astromech), the material used, and the various options that a particular droid has. The Jawa will choose the various options for a specific droid when adding that droid to the list of droids.

A Jawa will be presented with a user interface to add a new Droid, or print the current Droid collection. Adding a new Droid will require input from the Jawa to create the new droid. Once all of the needed information is collected for the droid, the new droid will be added to the droid collection.

If a Jawa decides to print the collection of droids in inventory, the program should loop through all of the droids in the collection and print out all of the various properties of each droid as well as the total cost of the droid. You should try to use a combination of the `__str__` and `total_cost` method/attribute along with Polymorphism to reduce the amount of code needed to print the results of each droid.
**NOTE:** You may want to print each droid as a block of text rather than trying to cram all of the various properties for the droid onto a single line.

All of the prices for the various aspects of a droid are left up to you to determine. If I was doing it though, I would probably have a small set price for each of the following general options, and not get too specific to save time. ie:
1. A price for the droid model (protocol, utility, etc.)
2. A few different material choices (Something made up), each with a different price. Have at least 4 choices.
3. A few different color choices (Something made up), each with a different prince. Have at least 4 choices.
4. A price for each additional option. One of the various option bools listed below. (3 options selected * $10 per option = $30)
5. A price per quantity option such as: numberOfLanguages, and numberOfShips (3 ships * $10 per ship = $30)

The program comes with an Abstract Base Class (ABC) called `AbstractDroid` that must be implemented by subclasses and can **NOT** be altered. You **MUST** use it as is. It contains a public method called `calculate_total_cost`, and a public attribute called `total_cost`. The `calculate_total_cost` method should not return anything, so it's job is to access the properties of the droid and literally calculate the total cost and then store it in the `total_cost` variable. It should **NOT** return the total cost. It should only calculates it.
The `total_cost` attribute is how you will get access to the total cost of the droid. This will be zero until `calculate_total_cost` is called. Then it will have a value.
I don't want you to have `calculate_total_cost` return the calculated value because I wanted you to have to use both a method and a property in subclasses.
Failure to follow this requirement will mean zero points for those parts of the program that are not using it correctly.

You should put all of your user interface into a `UserInterface` class that will handle getting all of the necessary information from the Jawa, and display the feedback to the Jawa.

You should create a class for the collection of the Droids. The `DroidCollection` class should contain the list that holds the droids, and maintain any internal information needed to manage that list. It should have at least one and at most four `add` methods that will add droids to the list. Whether you use one method that then determines which type of droid to create and add to the list or four separate methods that each adds a specific type of droid to the list is up to you. The `UserInterface` class will prompt for the needed information to add a droid, and then when it has all of the info, it will send it to these `add` methods to get the droid added.

You should follow the concepts about inheritance talked about in class, and work hard at DRY (Don't Repeat Yourself) Principles.

**NOTE:** This is the main focus of this program. Utilize inheritance and polymorphism as efficiently as possible. The less duplicated code, the better you will do on this assignment.

### Classes

The following Droid classes can all be created in a file called `droids.py`. The only class that should not be in this file is the `AbstractDroid` that was provided to you and the `UserInterface` class, which should be in a file called `user_interface.py`.
In total, you will have the following python files:
* `main.py`
* `program.py`
* `abstract_droid.py`
* `droids.py`
* `user_interface.py`

The program should have another `Abstract Base Class` called `Droid` with the following variables, properties, constructors, methods, etc that inherits from the `AbstractDroid` class that is provided to you.

`Droid`:

* Variables: `material` (string), `color` (string), `total_cost` (float - required by ABC)
* Constructors: 2 parameter constructor (`string`, `string`)
* Public Methods:
	* `__str__`: return a formatted string containing the properties of the droid.
	* `calculate_total_cost`: Required by the ABC to calculate and store the total cost.
* Protected Methods:
	* Your Choice - But think about what might be able to be protected to save you work in derived classes.

There should be two child classes derived from the abstract class `Droid` with appropriate variables, methods and properties. Both of these droid types can be created by a Jawa in the system.

`Protocol`:

* Variables: `number_of_languages` (int)
* Constant: `COST_PER_LANGUAGE`
* Constructors: 3 parameter constructor (`string`, `string`, `int`)
	* Uses the base class (`Droid`) constructor
* Public Methods:
	* `__str__`: return a formatted string containing the variables
	* `calculate_total_cost`: Calculate the `total_cost` based on the number of languages and droid type. Then add those values to any costs that can be calculated by the base class.
* Protected Methods:
	* Your Choice - But think about what might be able to be protected to save you work in derived classes.

`Utility`:

* Variables: `toolbox` (bool), `computerConnection` (bool), `scanner` (bool)
* Constructors: 5 parameter constructor (`string`, `string`, `bool`, `bool`, `bool`)
	* Uses the base class (`Droid`) constructor
* Public Methods:
	* `__str__`: return a formatted string containing the variables
	* `calculate_total_cost`: Calculates `total_cost` by calculating the cost of each selected option and droid type. Then add those values to any costs that can be calculated by the base class.
* Protected Methods:
	* Your Choice - But think about what might be able to be protected to save you work in derived classes.

There should be two more derived classes from the class `Utility` with appropriate variables, methods and properties.
**NOTE:** Even though `Utility` is the base class for these droids, `Utility` itself is still a valid droid option that can be created in the system.

`Janitor`:

* Variables: `broom` (bool), `vacuum` (bool)
* Constructors: 7 parameter constructor (`string`, `string`, `bool`, `bool`, `bool`, `bool`, `bool`)
	* Uses the base class (`Utility`) constructor
* Public Methods:
	* `__str__`: return a formatted string containing the variables
	* `calculate_total_cost`: Calculate `total_cost` by calculating the cost of each selected option and droid type. Then add those values to any costs that can be calculated by the base class.
* Protected Methods:
	* Your Choice - But think about what might be able to be protected to save you work in derived classes.

`Astromech`:

* Variables: `navigation` (bool), `number_of_ships` (int)
* Constant: `COST_PER_SHIP`
* Constructors: 7 parameter constructor (`string`, `string`, `bool`, `bool`, `bool`, `bool`, `int`)
	* Uses the base class (`Utility`) constructor
* Public Methods:
	* `__str__`: return a formatted string containing the variables
	* `calculate_total_cost`: Calculate totalCost by calculating the cost of each selected option, the cost based on the number of ships, and the droid type. Then add those values to any costs that can be calculated by the base class.
* Protected Methods:
	* Your Choice - But think about what might be able to be protected to save you work in derived classes.

![Droid Class Diagram](https://barnesbrothers.ddns.net/cis226/assignmentImages/assignment_3.png "Droid Class Diagram")

### Solution Requirements

Solution Must:

* Allow Jawa to add a new droid of either (`Protocol`, `Utility`, `Janitor`, or `Astromech`) to the list
* Allow Jawa to print the list of droids out.
* Do **NOT** make any changes to the `AbstractDroid` class.
* Do **NOT** change the method signature or return type of the `calculate_total_cost` method
* Create abstract class `Droid` that implements `AbstractDroid`
* Derive two classes (`Protocol` and `Utility`) from the class `Droid`
* Derive two classes (`Janitor` and `Astromech`) from the class `Utility`
* Each derived class (`Protocol`, `Utility`, `Janitor`, and `Astromnech`) must either override the `__str__` and `calculate_total_cost` methods or elegantly use functionality from its parent to achieve what it needs.
* Create a `UserInterface` class
* Create a `DroidCollection` class
* Use `private`, `protected`, and `public` access modification appropriately.
* Use `@abstractmethod` decorator appropriately.
* Have sufficient comments about what you are doing in the code.

#### Notes

If you did not do well on Assignment 1, you may want to look at the Assignment 1 Key that I did for some help related to UI classes, Collection classes, and structure.

It may be beneficial for you to create extra methods within the droid sub classes. You are not limited to the ones mentioned. You may even find it useful to make some additional ones that are protected.

You may not need to override the `__str__` method in child classes. You certainly can. But, if you do, you should try to delegate as much as possible to the parent class and only change what is needed for the child. The same goes for the `calculate_total_cost` method. The child classes should not be redoing the work of their parents if a call to the parents version can achieve the same effect.
