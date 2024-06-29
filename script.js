document.addEventListener('DOMContentLoaded', function() {
  // 페이지가 로드되면 실행될 함수를 등록한다. DOMContentLoaded 이벤트는 HTML 문서의 모든 요소가 로드되었을 때 발생한다.

  // JSON 파일을 fetch() 함수로 가져오기
  fetch('table.json')
      .then(response => response.json()) // JSON 형식의 응답을 자바스크립트 객체로 변환한다.
      .then(data => {
          const characters = Object.values(data); // JSON 데이터에서 캐릭터 배열을 추출한다.

          // HTML 테이블에 데이터 삽입
          const tableBody = document.getElementById('characterData'); // 캐릭터 데이터를 넣을 테이블의 tbody 요소를 가져온다.
          characters.forEach(character => {
              const row = document.createElement('tr'); // 각 캐릭터에 대한 새로운 행(tr) 요소를 생성한다.
              row.innerHTML = `
                  <td>${character.Name}</td>
                  <td>${character.Combat}</td>
                  <td>${character.level}</td>
                  <td><img src="${character.image}" alt="${character.Name}"></td>
                  <td>${character.Liberation ? 'Yes' : 'No'}</td>
              `; // 각 캐릭터의 정보를 테이블 셀(td)에 넣는다.
              tableBody.appendChild(row); // 생성한 행을 테이블에 추가한다.
          });

          // 전직업 달성률 계산 및 추가
          const totalCharacters = characters.length; // 전체 캐릭터 수
          const jobChangeAchievementRate = calculateJobChangeAchievementRate(characters); // 전직업 달성률 계산
          const liberationAchievementRate = calculateLiberationAchievementRate(characters); // 해방 달성률 계산

          const statsDiv = document.querySelector('.stats'); // 전직업 및 해방 달성률을 보여줄 div 요소를 가져온다.
          statsDiv.innerHTML += `
              <p>전직업 1억 달성률: <strong>${jobChangeAchievementRate.toFixed(2)}%</strong></p>
              <p>전직업 해방 달성률: <strong>${liberationAchievementRate.toFixed(2)}%</strong></p>
          `; // 계산된 달성률을 HTML에 추가한다.
      })
      .catch(error => {
          console.error('Error fetching JSON:', error); // JSON 가져오기 오류가 발생한 경우 콘솔에 오류 메시지를 출력한다.
      });

  // 전직업 달성률 계산 함수
  function calculateJobChangeAchievementRate(characters) {
      const totalCharacters = characters.length; // 전체 캐릭터 수
      const jobChangeCount = characters.filter(character => character.Combat >= 100000000).length; // 전직업 달성한 캐릭터 수
      return (jobChangeCount / totalCharacters) * 100; // 전직업 달성률을 계산하여 반환한다.
  }

  // 해방 달성률 계산 함수
  function calculateLiberationAchievementRate(characters) {
      const totalCharacters = characters.length; // 전체 캐릭터 수
      const liberationCount = characters.filter(character => character.liberation === true).length; // 해방 달성한 캐릭터 수
      return (liberationCount / totalCharacters) * 100; // 해방 달성률을 계산하여 반환한다.
  }
});
