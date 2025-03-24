function addExperience() {
    const expDiv = document.createElement('div');
    expDiv.className = 'experience';
    expDiv.innerHTML = `
        <input placeholder="Job Title" class="title">
        <input placeholder="Company Name" class="company">
        <input placeholder="Start Month/Year" class="start">
        <input placeholder="End Month/Year or Present" class="end">
        <textarea placeholder="Job Description" class="description"></textarea>
    `;
    document.getElementById('experiences').appendChild(expDiv);
}

function submitForm() {
    const experiences = Array.from(document.getElementsByClassName('experience')).map(exp => ({
        company: exp.querySelector('.company').value,
        title: exp.querySelector('.title').value,
        start: exp.querySelector('.start').value,
        end: exp.querySelector('.end').value,
        description: exp.querySelector('.description').value,
    }));
    

    const resumeData = {
        name: document.getElementById('name').value,
        phone: document.getElementById('phone').value,
        city: document.getElementById('city').value,
        state: document.getElementById('state').value,
        biography: document.getElementById('biography').value,
        skills: document.getElementById('skills').value,
        experiences: experiences,
        school: document.getElementById('school').value,
        major: document.getElementById('major').value,
        job_description: document.getElementById('job_description').value,
        certifications: document.getElementById('certifications').value,
    };

    // Display original resume
    document.getElementById('original').innerText = formatOriginalResume(resumeData);

    const startTime = performance.now();

    fetch('http://localhost:5000/generate_resume', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(resumeData),
    })
    .then(res => res.json())
    .then(data => {
        const endTime = performance.now();
        const duration = ((endTime - startTime) / 1000).toFixed(2);
        document.getElementById('result').innerText = data.tailored_resume;
        document.getElementById('time').innerText = `(Generated in ${duration} seconds)`;
    })
    .catch(err => alert('Error: ' + err.message));
}

function formatOriginalResume(data) {
    let output = `${data.name}\n${data.phone} | ${data.city}, ${data.state}\n\n`;
    output += `Professional Summary:\n${data.biography}\n\n`;
    output += `Skills:\n${data.skills}\n\n`;
    output += `Work Experience:\n`;
    data.experiences.forEach(exp => {
        output += `\n${exp.company} (${exp.start} - ${exp.end}):\n${exp.description}\n`;
    });
    output += `\nEducation:\n${data.school} – ${data.major}`;
    return output;
}
