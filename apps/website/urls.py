from django.urls import (path, include)

from . views import (
    index,
    people,
        #Lists Views
        ranks, 
        principalConsultants, 
        seniorConsultants,
        consultants, 
        seniorProfessionals,
        professionals,
        assistantProfessionals, 
        probationers,
        supportingTeam,
        nationalServicePersonnel, 

        # Detail Views
        principalConsultantsDetails,
        seniorConsultantDetails,
        consultantDetails,
        seniorProfessionalDetails,
        
    practice,
        history, 
        mandate, 
        functions,
        missionVisionAndValues,
        sectorMinistry, 
        corporateGovernance, 
        boardChairman,
        boardMember,
        services,
        management, 
        managingDirectorDetails,
        deputyManagingDirectorDetails, 
        headsOfDepartmentsDetails,
        regionalConsultantDetails, 
        alliances,
        clientSpeak, 
        corporateResponsibilities,

    principles, 
        professionalism,
        civic, 
        excellence,
        integrityAndHonesty, 
        timelinessAndCostEffectiveness, 
        sustainability, 
        empowerment, 

    projects,
        projectsList,
        projectsMap, 
        projectFilms, 
        projectDetails,
        projectCategories,
        projectCategoryDetails, 
        projectCategoryCreate, 
        projectSubCategories, 
        projectSubCategories, 
    search,

    news,

    publications,
    test2,
    policiesAndGuidelines
)

app_name = 'website'

urlpatterns = [
    # Tests
    path('tests/', test2, name='test2'),
    # Tests
    path('policies-and-guidelines/', policiesAndGuidelines, name='policies-and-guideslines'),
    # Home Page
    path('', index, name='index'),
    # People
    path('people/',include
        (
            [
                path('', 
                    people, 
                    name='people-home'),

                path('<slug:slug>/', 
                    ranks, 
                    name='ranks'),

                path('aesl-consultants/principal-consultants/', 
                    principalConsultants, 
                    name='principal-consultants'),

                path('aesl-consultants/principal-consultants/principal-consultant-details', 
                    principalConsultantsDetails, 
                    name='principal-consultant-details'),
                
                path('aesl-consultants/senior-consultants/', 
                    seniorConsultants, 
                    name='senior-consultants'),

                path('aesl-consultants/senior-consultants/senior-consultant-details', 
                    seniorConsultantDetails, 
                    name='senior-consultant-details'),
                
                path('aesl-consultants/consultants\'/', 
                    consultants, 
                    name='consultants'),
                    
                path('aesl-consultants/consultants/consultant-details', 
                    consultantDetails, 
                    name='consultant-details'),
                
                path('senior-professionals/', 
                    seniorProfessionals, 
                    name='senior-professionals'),

                path('senior-professionals/senior-professional-details', 
                    seniorProfessionalDetails, 
                    name='senior-professional-details'),
                
                path('professionals', 
                    professionals, 
                    name='professionals'),

                path('assistant-professionals', 
                    assistantProfessionals, 
                    name='assistant-professionals'),

                path('probationers', 
                    probationers, 
                    name='probationers'),

                path('supporting-team', 
                    supportingTeam, 
                    name='supporting-team'),

                path('service-personnel', 
                    nationalServicePersonnel, 
                    name='national-service-personnels'),
            ]
        )
    ),
        
    # Practice
    path('practice/', include
            (
                [
                    path('', 
                        practice, 
                        name = 'practice-home'),
                    path('history', 
                        history, 
                        name = 'history'),
                    path('mandate', 
                        mandate, 
                        name = 'mandate'),
                    path('functions', 
                        functions, name  = 'functions'),    
                    path('mission-vision-values', 
                        missionVisionAndValues, 
                        name = 'mission-vision-values'), 
                    
                    path('corporate-governance/', 
                        corporateGovernance, 
                        name = 'corporate-governance'),
                    path('corporate-governance/board-chairman-details', 
                        boardChairman, 
                        name = 'corporate-governance-board-chairman'),
                    path('corporate-governance/board-members/board-member-details', 
                        boardMember, 
                        name = 'corporate-governance-board-member'),
                    
                    path('management/', 
                        management, 
                        name = 'management'),                    
                    path('management/managing-director-details', 
                        managingDirectorDetails, 
                        name = 'managing-director'),
                    path('management/deputy-managing-director-details', 
                        deputyManagingDirectorDetails, 
                        name = 'deputy-managing-director'),
                    path('management/heads-of-departments/head-of-department-details', 
                        headsOfDepartmentsDetails, 
                        name = 'head-of-department-details'),
                    path('management/regional-consultants/regional-consultant-details', 
                        regionalConsultantDetails, 
                        name = 'regional-consultant-consultant-details'),                 
                    path('sector-ministry', 
                        sectorMinistry, 
                        name = 'sector-ministry'),
                    path('alliances/', 
                        alliances, name ='alliances'),
                    path('client-speak', 
                        clientSpeak, 
                        name = 'client-speak'),
                    path('corporate-responsibilities', 
                        corporateResponsibilities, 
                        name = 'corporate-responsibilities'),
                    path('services', 
                        services, 
                        name = 'services'),
                ]
            )
        ),
    
    # Principles
    path('principles/', include([
            path('', 
                principles, 
                name = 'principles-home'),
            path('professionalism', 
                professionalism, 
                name = 'principles-professionalism'),
            path('civic', 
                civic, 
                name = 'principles-civic'),
            path('excellence', 
                excellence, 
                name = 'principles-excellence'),
            path('integrity-and-honesty', 
                integrityAndHonesty, 
                name = 'principles-integrity-and-honesty'),
            path('timeliness-and-cost-effectiveness', 
                timelinessAndCostEffectiveness, 
                name = 'principles-timeliness-and-cost-effectiveness'),
            path('sustainability', 
                sustainability, 
                name = 'principles-sustainability'),
            path('empowerment', 
                empowerment, 
                name = 'principles-empowerment'),])
    ),

    # Projects
    path('projects/', include
            (
                [
                    # Projects Home
                    path('', 
                        projects, 
                        name = 'projects-home'),
                    # Projects List
                    path('projects-list/', 
                        projectsList, 
                        name='projects-list'),
                    # Project Details
                    path('<slug:slug>', 
                        projectDetails, 
                        name='project-details'),
                    # Projects Map
                    path('projects-map-home/', 
                        projectsMap, 
                        name='projects-maps-home'),
                    # Project Films
                    path('projects-films-home/', 
                        projectFilms, 
                        name='project-films-home'),
            
                    # Project Categories Home
                    path('project-categories-home/', 
                        projectCategories, 
                        name='project-categories-home'),
                    # Project Categories List
                    path('project-categories-list/', 
                        projectCategories, 
                        name='project-categories-list'),
                    # Project Categories Details
                    path('<slug:slug>/', 
                        projectCategoryDetails, 
                        name='project-category-details'),
                    
                    # Project Category Create   
                    path('project-categories-create/', 
                        projectCategoryCreate, 
                        name='project-categories-create'),


                    path('project-sub-categories-home/', 
                        projectSubCategories, 
                        name='project-sub-categories-home'),

                    path('project-sub-categories-list/', 
                        projectSubCategories, 
                        name='project-sub-categories-list'),

                    path('<slug:slug>/', 
                        projectSubCategories, 
                        name='project-sub-categories-details'),

                    # path('project-types-home/', 
                    #   project_Types_Home, 
                    # name='project-types-home'),
                    # path('project-types-list/', 
                    #   project_Types_List, 
                    # name='project-types-list'),
                    # path('<slug:slug>/', 
                    #   project_Type_Details, 
                    # name='project-type-details'),
                ]
            )
        ),
    
    # Search
    path('search/', 
        search, 
        name = 'search'
        ),
    
    # News
    path('news/', 
        news, 
        name = 'news-home'),

    #Publications
    path('publications/', 
        publications, 
        name = 'publications-home'),
] 
    
