workspace "Name" "Description" {
    !identifiers hierarchical
    model {
        u1 = person "User 1"
        u2 = person "User 2" 

        ss = softwareSystem "Software System" {
            wa = container "Web Application"
            db = container "Database Schema" {
                tags "Database"
            }
        }

        aws = softwareSystem "AWS Environment" 

        u1 -> ss.wa "Uses"
        u1 -> aws "Deploys to" 
        u2 -> ss.wa "Uses" 

        ss.wa -> ss.db "Reads from and writes to"
    }
    views {
        systemContext ss "Diagram1" {
            include *
            include aws 
            autolayout lr
        }
        container ss "Diagram2" {
            include *
            autolayout lr
        }
        styles {
            element "Element" {
                color #ffffff
            }
            element "Person" {
                background #9b191f
                shape person
            }
            element "Software System" {
                background #ba1e25
            }
            element "Container" {
                background #d9232b
            }
            element "Database" {
                shape cylinder
            }
            element "AWS Environment" { 
                background #007bff 
            }
        }
    }
    configuration {
        scope softwaresystem
    }
}
