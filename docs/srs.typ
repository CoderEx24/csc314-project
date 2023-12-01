#let ProjectName = "LinkedIn"
#set par(justify: true)

#align(center, text(30pt)[
  #ProjectName Documentation
])

/*
= User Requirements
+ Customize profile
+ Control profile visiability
+ Register courses
+ Offer jobs
+ Recommend job offers
+ Add Experience, Education and skills
+ Allow endorsment
+ Social media
+ Chatting
*/

= Project Overview
- #ProjectName is a professional networking platform that connects professionals, businesses,
  and job seekers from around the world. The project's purpose is to facilitate professional connections, 
  foster career development, and enable knowledge sharing within various industries. 

- #ProjectName's primary goal is to provide a platform where professionals can showcase their skills, 
  experience, and achievements through their profile. It aims to create a professional community where 
  individuals can network, collaborate, and build relationships with others in their field. 


- The target audience for #ProjectName includes professionals from all industries, such as job seekers, 
  working professionals, recruiters, business owners, and entrepreneurs. 
  It also caters to companies looking to connect with potential employees and build their brand presence. 
  #ProjectName is designed to benefit individuals at all stages of their careers, 
  from entry-level professionals to experienced executives.


= Requirements
- The System shall allow users to create accounts. There shall be 2 types of accounts, Person and Company.
  Person represents regular people, while Company represents companies and other establishments.
- The System shall require a name, an email and a password in order to create a Person account. The System 
  should recommend using a password manager to the user.
- The System shall require a name, an email, an address, contact information and a password in order to create
  a Company account. The System should recommend using a password manager to the user.
- The System shall allow users with Person accounts to connect to and disconnect from each other. 
  The System shall recommend other Person accounts to connect to based on the current connections. 
  Connections allow users to send messages to each other, see each other's posts and see each other's followings.
- The System shall allow users with Person accounts to follow each other. Followers can view posts of
  accounts they follow. 
- The System shall allow users to make, edit and delete posts. Posts consists of text and can optionally 
  contain images and videos. The System could allow text formatting and typesetting.
- The System shall allow users to use reactions with the post. The System shall allow the poster to disable 
  reactions.
- The System shall allow users to post comments on posts. The System shall allow the poster to disable
  comments. The System could allow text formatting and typesetting in comments.
- The System shall allow users to share posts. Users can share posts with users they're connected with 
  already.
- The System shall allow users to publish their resume, skills, education and certificates on their profiles.
  The System shall allow users to upload files relating to their certificates and education.
- The System shall allow users of Company account type to post job posts. These posts will contain job title,
  salary range, description and required skills, education and certificates. The System shall show the 
  Company's contact information. The System shall allow users of type Company to make forms in order for
  users of type Person to apply to that job post. The System shall allow text input. The System could allow
  file upload.
- The System shall recommend job posts to users of type Person. The System shall recommend job posts according
  to the user's skills, education and certificates.
- The System shall allow users of type Person to apply to job posts.
- The System shall allow users to endorse skills of users in their connections. A skill can be endorse
  if and only if it is common between 2 connected users. Endorsements increases the rank of a profile.
  Users of type Company view applications to their job posts ordered by the rank of users of type Person.

= Roles and Responsibilities
#table(
  columns: (1fr, 0.7fr, 1.7fr),
  [Name], [ID], [Role & Responsibilities],
  [Kareem Hassanein Hassan], [320210201], 
  [
    *Developer* \
    Implementation, Unit & Integration testing
  ],
  [Amira Hatem], [320210193], 
  [
    *Stakeholder* \
    Requirement Specification, Acceptance testing
  ],
  [Mai Ibrahim], [320210312], 
  [
    *Business Analyst* \
    Requirement Specification and analysis
  ],
)	

= Timeline

#table(
  columns: (1fr, 1fr),
  [Task], [Deadline],
  [Phase 1], [10/11/2023],
  [Use case Diagram], [25/11/2023],
  [Analysis], [20/12/2023],
  [Implementation], [10/1/2024],
)

#pagebreak()

= Risk Assessment
Here are some key risks and corresponding mitigation strategies:

/ Data Security:
  There is a risk of unauthorized access to user data and potential data breaches. 
  Mitigation strategies could include implementing strong encryption protocols, regularly updating security measures, conducting security audits, and educating users about best practices for protecting their data.


/ Privacy Concerns: 
  Users may be concerned about the privacy of their personal information shared on the platform. 
  To mitigate this risk, the app should have transparent privacy policies, obtain user consent for data usage,
  and provide users with control over their privacy settings.

/ Fake Profiles and Scams: 
  There is a risk of fake profiles and scams that can harm the reputation and trustworthiness of the platform.
  Implementing robust profile verification processes, employing artificial intelligence algorithms 
  to detect suspicious activities, and encouraging users to report suspicious profiles can help 
  mitigate this risk.

/ Inappropriate Content: 
  Users may post or share inappropriate content on the platform, leading to negative user experiences. 
  Implementing content moderation systems, user reporting mechanisms, and community guidelines can 
  help identify and remove such content promptly.

/ Platform Abuse: 
  There is a risk of users engaging in spamming, harassment, or other forms of abusive behavior. 
  Implementing strong user guidelines, enforcing strict policies against abusive behavior, 
  and providing users with a reporting system can help mitigate this risk.

/ Technical Issues: 
  The app may experience technical issues like downtime, slow loading times, or glitches. 
  Regular maintenance, performance testing, and having a robust technical support system can help 
  minimize the impact of such issues on user experience.

/ Competition: 
  The app may face stiff competition from other similar platforms. Conducting thorough market research, 
  identifying unique features, and continuously innovating and improving the platform can help mitigate 
  this risk.
