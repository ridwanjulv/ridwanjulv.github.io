# Create Diagrams using MermaidJs

Create diagrams in markdown using [mermaid](http://mermaid.js.org/syntax/flowchart.html) fenced code blocks:

## Flowchart
more command in https://mermaid.js.org/syntax/flowchart.html

```mermaid
flowchart TD;
    A--note-->B;
    A-->C;
    B-->D["`Allow **bold** & _italic_`"];
    C(rounded)-->D([more rounded]);
    D-->E[[subroutine]];
    E-->F[(Database)];
    F-->G((Circle));
    I{decision}--true-->H;
    I{decision}--false-->J[\process\];
    H-.dotted.-J;
    H-.dotted arrow.->J;
    J==thick arrow==>K;
    K <--> l;
    K -----> m[longerlink];
```
```mermaid
flowchart LR;
    A["predefined text and unicode 😋"]
    D[Another predefined node]
    A-->C;
    B-->D;
    subgraph one
    A-->B
    end
    subgraph two
    C-->D
    D-->three
    end
    subgraph three[alias]
    c1-->c2
    end
    three-->one;
    id1----id2;
    style id1 fill:#f9f,stroke:#333,stroke-width:4px
    style id2 fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5
    A & B:::bar --> C:::foobar
    classDef foo stroke:#f00
    classDef bar stroke:#0f0
    classDef foobar stroke:#00f
```
## State Diagram
more command in https://mermaid.js.org/syntax/stateDiagram.html
```mermaid
stateDiagram-v2
    direction LR
    classDef notMoving fill:white
    classDef movement font-style:italic;
    classDef badBadEvent fill:#f00,color:white,font-weight:bold,stroke-width:2px,stroke:yellow

    Still:::notMoving : This is a state description 
    state if_state <<choice>>
    Crash:::badBadEvent
    Continue:::movement
    state Moving {
        [*] --> speeding
        speeding --> [*]
    }

    [*] --> Still
    Still --> [*]: A transition

    Still --> Moving
    Moving --> Still
    Moving --> if_state
    Crash --> [*]
    if_state --> Continue: if n < 0
    if_state --> Crash : if n >= 0
    note right of Moving
            Important information! You can write
            notes.
        end note
    note left of Crash : This is the note to the left.
```
concurrent state diagram:
```mermaid
stateDiagram-v2
    [*] --> Active

    state Active {
        [*] --> NumLockOff
        NumLockOff --> NumLockOn : EvNumLockPressed
        NumLockOn --> NumLockOff : EvNumLockPressed
        --
        [*] --> CapsLockOff
        CapsLockOff --> CapsLockOn : EvCapsLockPressed
        CapsLockOn --> CapsLockOff : EvCapsLockPressed
        --
        [*] --> ScrollLockOff
        ScrollLockOff --> ScrollLockOn : EvScrollLockPressed
        ScrollLockOn --> ScrollLockOff : EvScrollLockPressed
    }
```
```mermaid
stateDiagram-v2
    classDef gen2 fill:#f55
    classDef gen1 fill:#c95
    classDef gen0 fill:#990
    classDef you fill:#f00
    classDef gen_1 fill:#660
    classDef gen_2 fill:#099

    state couple1da <<choice>>
    aunt_d --> couple1da
    uncle_d --> couple1da
    couple1da --> cousin:::gen0

    state couple2m <<choice>>
    granpa_m --> couple2m
    granma_m --> couple2m
    couple2m --> mom:::gen1
    couple2m --> uncle_m:::gen1

    state couple2d <<choice>>
    granpa_d --> couple2d
    granma_d --> couple2d
    couple2d --> dad:::gen1
    couple2d --> aunt_d:::gen1
    class granma_m,granpa_m,granma_d,granpa_d  gen2

    state couple1b <<choice>>
    brother --> couple1b
    systerInLaw_b --> couple1b
    couple1b --> nephew:::gen_1

    state couple1 <<choice>>
    dad --> couple1
    mom --> couple1
    couple1 --> brother:::gen0
    couple1 --> syster:::gen0
    couple1 --> you:::you

    state couple1m <<choice>>
    dadInLaw --> couple1m
    momInLaw --> couple1m
    couple1m --> brotherInLaw_m:::gen0
    couple1m --> systerInLaw_m:::gen0
    couple1m --> mate:::gen0
    class systerInLaw_b gen0
    class uncle_d,momInLaw, dadInLaw  gen1

    state couple+1s <<choice>>
    son --> couple+1s
    daughterInLaw --> couple+1s
    couple+1s --> grandson_s:::gen_2
    couple+1s --> granddaughter_s:::gen_2

    state couple0 <<choice>>
    you --> couple0
    mate --> couple0
    couple0 --> son:::gen_1
    couple0 --> daughter:::gen_1

    state couple+1d <<choice>>
    daughter --> couple+1d
    sonInLaw --> couple+1d
    couple+1d --> grandchild:::gen_2

    class sonInLaw,daughterInLaw gen_1
```
## Sequence Diagram
more command in https://mermaid.js.org/syntax/sequenceDiagram.html
```mermaid
sequenceDiagram
    autonumber
    box purple Main
    participant A as Alice
    participant Bob
    end
    box rgb(33,66,99)
    actor John
    end
    A->>John: Hello John, how are you?
    loop Healthcheck
        John->>John: Fight against hypochondria
        John-)Alice: help!
        Alice-)John: Coming
    end
    Note right of John: Rational thoughts <br/>prevail!
    John-->>A: Great!
    rect rgb(200, 150, 255)
    note right of Alice: Alice calls John.
    Alice->>+John: Hello John, how are you?
    end
    Alice->>+John: John, can you hear me?
    John-->>-Alice: Hi Alice, I can hear you!
    John-->>-Alice: I feel great!
    Note over Alice,John: A typical interaction<br/>But now in two lines
    alt is sick
        Bob->>Alice: Not so good :(
    else is well
        Bob->>Alice: Feeling fresh like a daisy
    end
    opt Extra response
        Bob->>Alice: Thanks for asking
    end
```
supported arrow:
| Type | Description                                      |
| ---- | ------------------------------------------------ |
| ->   | Solid line without arrow                         |
| -->  | Dotted line without arrow                        |
| ->>  | Solid line with arrowhead                        |
| -->> | Dotted line with arrowhead                       |
| -x   | Solid line with a cross at the end               |
| --x  | Dotted line with a cross at the end.             |
| -)   | Solid line with an open arrow at the end (async) |
| --)  | Dotted line with a open arrow at the end (async) |

```mermaid
sequenceDiagram
    participant web as Web Browser
    participant blog as Blog Service
    participant account as Account Service
    participant mail as Mail Service
    participant db as Storage

    Note over web,db: The user must be logged in to submit blog posts
    web->>+account: Logs in using credentials
    account->>db: Query stored accounts
    db->>account: Respond with query result

    alt Credentials not found
        account->>web: Invalid credentials
    else Credentials found
        account->>-web: Successfully logged in

        Note over web,db: When the user is authenticated, they can now submit new posts
        web->>+blog: Submit new post
        blog->>db: Store post data

        par Notifications
            blog--)mail: Send mail to blog subscribers
            blog--)db: Store in-site notifications
        and Response
            blog-->>-web: Successfully posted
        end
    end
```

## Class Diagram
more command in https://mermaid.js.org/syntax/classDiagram.html
```mermaid
classDiagram
Class01 <|-- AveryLongClass : Cool
Class03 *-- Class04
Class05 o-- Class06
Class07 .. Class08
Class09 --> C2 : Where am i?
Class09 --* C3
Class09 --|> Class07
Class07 : equals()
Class07 : Object[] elementData
Class01 : size()
Class01 : int chimp
Class01 : int gorilla
Class08 <--> C2: Cool label
```

## Git Graph
more command in https://mermaid.js.org/syntax/gitgraph.html
```mermaid
gitGraph
   commit
   commit
   branch develop
   checkout develop
   commit
   commit
   checkout main
   commit
   merge develop
   commit  id:"Alpha" tag:"v0.0.1"
   commit
```
```mermaid
gitGraph:
    commit "Ashish"
    branch newbranch
    checkout newbranch
    commit id:"1111"
    commit tag:"test"
    checkout main
    commit type: HIGHLIGHT id:"Beta"
    commit
    merge newbranch
    commit
    branch b2
    commit
```

## ER Diagram
more command in https://mermaid.js.org/syntax/entityRelationshipDiagram.html
```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE-ITEM : contains
    CUSTOMER }|..|{ DELIVERY-ADDRESS : uses
    CAR ||--o{ NAMED-DRIVER : allows
    CAR {
        string registrationNumber
        string make
        string model
    }
    PERSON ||--o{ NAMED-DRIVER : is
    PERSON {
        string firstName
        string lastName
        int age
    }
```
```
|   one
||  one and only one
o|  zero or one
{   many
o{  zero or many
1{  one or many

```

## Quadrant Chart
```mermaid
more command in https://mermaid.js.org/syntax/quadrantChart.html
quadrantChart
    title Reach and engagement of campaigns
    x-axis Low Reach --> High Reach
    y-axis Low Engagement --> High Engagement
    quadrant-1 We should expand
    quadrant-2 Need to promote
    quadrant-3 Re-evaluate
    quadrant-4 May be improved
    Campaign A: [0.3, 0.6]
    Campaign B: [0.45, 0.5]
    Campaign C: [0.57, 0.69]
    Campaign D: [0.78, 0.34]
    Campaign E: [0.40, 0.34]
    Campaign F: [0.35, 0.78]
```

## Pie Chart
```mermaid
pie 
title Pets adopted by volunteers
    "Dogs" : 386
    "Cats" : 85
    "Rats" : 15
```
```mermaid
pie showData
    title Key elements in Product X
    "Calcium" : 42.96
    "Potassium" : 50.05
    "Magnesium" : 10.01
    "Iron" :  5
```

## Mind Map
more command in 
```mermaid
mindmap
  root((mindmap))
    Origins
      Long history
      ::icon(fa fa-book)
      Popularisation
        British popular psychology author Tony Buzan
    Research
      On effectiveness<br/>and features
      On Automatic creation
        Uses
            Creative techniques
            Strategic planning
            Argument mapping
    Tools
      Pen and paper
      Mermaid
```