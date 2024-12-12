'''
Танд нийт numCourses хичээл байх бөгөөд эдгээрийг 0-оос numCourses - 1 хүртэл нэрлэнэ. Та prerequisites массивыг өгч байна, энд prerequisites[i] = [ai, bi] гэдэг нь курс ai-г авахын тулд курс bi-г эхлээд авах шаардлагатай гэдгийг илэрхийлнэ.

Жишээ нь, [0, 1] хослол нь курс 0-г авахын тулд курс 1-ийг эхлээд авах хэрэгтэйг заана. Танд хичээлүүдийг дуусгахын тулд ямар дараалалтайгаар авахыг зааж өгөх шаардлагатай. 
'''

def findOrder(numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)}  
    for course, prereq in prerequisites:
        graph[prereq].append(course) 
    
    visited = [0] * numCourses  # 0 gedeg ni kursiig shalgaagui
    result = []  #
    
    def dfs(course):
        if visited[course] == 1: 
            return False
        if visited[course] == 2: 
            return True
        
        visited[course] = 1  # bolovsruulj ehelsen

        for next_course in graph[course]:
            if not dfs(next_course): 
                return False

        visited[course] = 2  
        result.append(course)  
        return True

    for course in range(numCourses):
        if visited[course] == 0:  # shalgaagui dfs hiin
            if not dfs(course): 
                return []  

    return result[::-1]

# Тестлэх жишээ
print(findOrder(2, [[1, 0]]))  
