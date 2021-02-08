function formSubmit()
{
    document.getElementById("don_form").submit();
}

function get_institution()
{
  var markedCheckbox = document.querySelectorAll('input[type="checkbox"]:checked');
  var cats_ids = [];
  markedCheckbox.forEach(checkbox=>cats_ids.push(checkbox.value))
   console.log(cats_ids);
  var addres = '/get_institution?';
  for(var i=0;i<cats_ids.length; i++)
  {
    addres = addres + "cat_id=" +cats_ids[i]+'&'
  }
     fetch(addres)
        .then(response => response.text())
        .then(data => document.getElementById("institutions").innerHTML = data);
  console.log(addres)
}

function handle_form()
{
  let form = document.getElementById("don_form");
  let summary = document.getElementById("summary");
  let fd = new FormData(form);
  fd.delete('csrfmiddlewaretoken');
  let ul = document.createElement('ul');
  for (let value of fd.values()) {
    let li = document.createElement('li', )
    li.innerHTML = value
    ul.appendChild(li)

  }
  summary.innerHTML = ""
  summary.appendChild(ul)

}
function checkbox_val()
{
  let check = document.querySelectorAll('input[type="checkbox"]:checked').length;
  if (check > 0) {
    console.log('Good');}
  else {console.log('You didn\'t choose any of the checkboxes!');
  return false;}
}

function validate_orgs()
{
  let check = document.querySelectorAll('input[type="radio"]:checked').length;
  if (check > 0) {
    console.log('Good');}
  else {console.log('You didn\'t choose any of the checkboxes!');
  return false;}
}

function validate_bags() {
  let bags = document.getElementById('bags');
  if (!bags.value == "") {
    console.log('jest ok');
    } else {console.log('braki');
    return false;}
}
function validate_address() {
  let street = document.getElementById('street');
  let city = document.getElementById('city');
  let zip = document.getElementById('street');
  let phone = document.getElementById('phone');
  let date = document.getElementById('date');
  let time = document.getElementById('time');

  if (street.value == "" || city.value == "" || zip.value == "" || phone.value == "" || date.value == "" || time.value == "") {
    console.log('braki');
    return false
    } else {console.log('jest ok');
    return true;}
  }


document.addEventListener("DOMContentLoaded", function() {
  /**
   * HomePage - Help section
   */
  class Help {
    constructor($el) {
      this.$el = $el;
      this.$buttonsContainer = $el.querySelector(".help--buttons");
      this.$slidesContainers = $el.querySelectorAll(".help--slides");
      this.currentSlide = this.$buttonsContainer.querySelector(".active").parentElement.dataset.id;
      this.init();
    }

    init() {
      this.events();
    }

    events() {
      /**
       * Slide buttons
       */
      this.$buttonsContainer.addEventListener("click", e => {
        if (e.target.classList.contains("btn")) {
          this.changeSlide(e);
        }
      });

      /**
       * Pagination buttons
       */
      this.$el.addEventListener("click", e => {
        if (e.target.classList.contains("btn") && e.target.parentElement.parentElement.classList.contains("help--slides-pagination")) {
          this.changePage(e);
        }
      });
    }

    changeSlide(e) {
      e.preventDefault();
      const $btn = e.target;

      // Buttons Active class change
      [...this.$buttonsContainer.children].forEach(btn => btn.firstElementChild.classList.remove("active"));
      $btn.classList.add("active");

      // Current slide
      this.currentSlide = $btn.parentElement.dataset.id;

      // Slides active class change
      this.$slidesContainers.forEach(el => {
        el.classList.remove("active");

        if (el.dataset.id === this.currentSlide) {
          el.classList.add("active");
        }
      });
    }

    /**
     * TODO: callback to page change event
     */
    changePage(e) {
      e.preventDefault();
      const page = e.target.dataset.page;

      console.log(page);
    }
  }
  const helpSection = document.querySelector(".help");
  if (helpSection !== null) {
    new Help(helpSection);
  }

  /**
   * Form Select
   */
  class FormSelect {
    constructor($el) {
      this.$el = $el;
      this.options = [...$el.children];
      this.init();
    }

    init() {
      this.createElements();
      this.addEvents();
      this.$el.parentElement.removeChild(this.$el);
    }

    createElements() {
      // Input for value
      this.valueInput = document.createElement("input");
      this.valueInput.type = "text";
      this.valueInput.name = this.$el.name;

      // Dropdown container
      this.dropdown = document.createElement("div");
      this.dropdown.classList.add("dropdown");

      // List container
      this.ul = document.createElement("ul");

      // All list options
      this.options.forEach((el, i) => {
        const li = document.createElement("li");
        li.dataset.value = el.value;
        li.innerText = el.innerText;

        if (i === 0) {
          // First clickable option
          this.current = document.createElement("div");
          this.current.innerText = el.innerText;
          this.dropdown.appendChild(this.current);
          this.valueInput.value = el.value;
          li.classList.add("selected");
        }

        this.ul.appendChild(li);
      });

      this.dropdown.appendChild(this.ul);
      this.dropdown.appendChild(this.valueInput);
      this.$el.parentElement.appendChild(this.dropdown);
    }

    addEvents() {
      this.dropdown.addEventListener("click", e => {
        const target = e.target;
        this.dropdown.classList.toggle("selecting");

        // Save new value only when clicked on li
        if (target.tagName === "LI") {
          this.valueInput.value = target.dataset.value;
          this.current.innerText = target.innerText;
        }
      });
    }
  }
  document.querySelectorAll(".form-group--dropdown select").forEach(el => {
    new FormSelect(el);
  });

  /**
   * Hide elements when clicked on document
   */
  document.addEventListener("click", function(e) {
    const target = e.target;
    const tagName = target.tagName;

    if (target.classList.contains("dropdown")) return false;

    if (tagName === "LI" && target.parentElement.parentElement.classList.contains("dropdown")) {
      return false;
    }

    if (tagName === "DIV" && target.parentElement.classList.contains("dropdown")) {
      return false;
    }

    document.querySelectorAll(".form-group--dropdown .dropdown").forEach(el => {
      el.classList.remove("selecting");
    });
  });

  /**
   * Switching between form steps
   */
  class FormSteps {
    constructor(form) {
      this.$form = form;
      this.$next = form.querySelectorAll(".next-step");
      this.$prev = form.querySelectorAll(".prev-step");
      this.$step = form.querySelector(".form--steps-counter span");
      this.currentStep = 1;

      this.$stepInstructions = form.querySelectorAll(".form--steps-instructions p");
      const $stepForms = form.querySelectorAll("form > div");
      this.slides = [...this.$stepInstructions, ...$stepForms];

      this.init();
    }

    /**
     * Init all methods
     */
    init() {
      this.events();
      this.updateForm();
    }

    /**
     * All events that are happening in form
     */
    events() {
      // Next step
      this.$next.forEach(btn => {
        btn.addEventListener("click", e => {
          e.preventDefault();
          this.currentStep++;
          this.updateForm();
        });
      });

      // Previous step
      this.$prev.forEach(btn => {
        btn.addEventListener("click", e => {
          e.preventDefault();
          this.currentStep--;
          this.updateForm();
        });
      });

      // Form submit
      this.$form.querySelector("form").addEventListener("submit", e => this.submit(e));
    }

    /**
     * Update form front-end
     * Show next or previous section etc.
     */
    updateForm() {
      this.$step.innerText = this.currentStep;
      if (this.currentStep > 1) {
        if (checkbox_val() == false) {
          alert('Choose categories');
          this.currentStep = 1;
        }

      }
      if (this.currentStep > 2) {
        if (validate_bags() == false) {
          alert('Give number of bags');
          this.currentStep = 2;
        }
      }
      if (this.currentStep > 3) {
        if (validate_orgs() == false) {
          alert('Choose organisation');
          this.currentStep = 3;
        }
      }
            if (this.currentStep > 4) {
        if (validate_address() == false) {
          alert('Fill up missing data');
          this.currentStep = 4;
        }
      }

      if (this.currentStep==3)
       {
         get_institution();
       }
      if (this.currentStep==5)
       {
         handle_form();
       }


      // TODO: Validation

      this.slides.forEach(slide => {
        slide.classList.remove("active");

        if (slide.dataset.step == this.currentStep) {
          slide.classList.add("active");
        }
      });

      this.$stepInstructions[0].parentElement.parentElement.hidden = this.currentStep >= 6;
      this.$step.parentElement.hidden = this.currentStep >= 6;

      // TODO: get data from inputs and show them in summary
    }

    /**
     * Submit form
     *
     * TODO: validation, send data to server
     */
    submit(e) {
      e.preventDefault();
      formSubmit();
      this.currentStep++;
      this.updateForm();
    }
  }
  const form = document.querySelector(".form--steps");
  if (form !== null) {
    new FormSteps(form);
  }
});
