# FactorioCalcBase
계산기의 본체입니다.

<h2>data</h2>
Factorio의 레시피와 생산시설, 모듈 정보 등의 데이터입니다. 

<h2>recipe_class.py</h2>

>recipe_name 인자를 받아 레시피 객체를 생성합니다.
>
>><h4>get_category()</h4>
카테고리를 확인합니다. 카테고리가 따로 기입되지 않은 경우, 'crafting'으로 분류합니다.
>
>><h4>is_name_results_match()</h4>
>>
>>레시피의 이름과 결과물이 일치하는지 확인합니다.
>> 
>>대부분은 결과물과 레시피의 이름이 일치합니다. 일치하지 않는 경우 계산을 위해 추가적인 과정이 필요합니다.
>
>><h4>get_results_count()</h4>
>>결과물의 개수를 확인합니다. 
>>
>>대부분의 레시피는 결과물이 1개이지만, 그렇지 않은 경우가 존재합니다.
>>
>>레시피의 결과물이 한 종류 이상일 경우엔 -1을 반환합니다.

<h2>production_machine.py</h2>
>팩토리오의 생산시설 정보(**data.binary.production_machine_dict**)를 바탕으로 머신 객체를 생성합니다. 

<h2>production_block.py</h2>
> <h3>ProductionBlock</h3>
> 레시피와 머신을 결합한 계산기의 기본단위입니다.
>><h4>get_available_machine_list()</h4> 
>> 레시피 객체의 **category**를 바탕으로 가능한 머신 리스트를 생성합니다. 기본값은 리스트의 맨 마지막(-1) 입니다.
>><h4>update_machine(machine_name: str)</h4>
>> 머신 객체를 다시 생성합니다. machine_name이 available_machine_list에 속하지 않을 경우에는 기존의 machine_name을 바탕으로 머신 객체가 다시 생성됩니다.
>><h4>set_module(module_code_or_list)</h4>
>> 모듈을 장착합니다. **can_this_module_be_added()** 메소드로 리스트 요소의 장착 가능 여부를 검사한 후, 추가합니다. 장착 불가능한 값을 전달하면 장착되지 않습니다.
>> 모듈을 장착한 후에는 **update_and_calculate_at_once()** 메소드를 통해 모듈 모디파이어를 적용합니다.
>><h4>calculate_total_modifier()</h4>
>> 장착된 모듈의 값을 **module_modifier_dict**에서 가져온 후 전부 합칩니다.
>> 채광 카테고리에 포함된 경우 **mining_research_modifier**의 값도 반영합니다.
>>
>> 기본적으로 팩토리오의 모디파이어는 합연산입니다.
>>
>>      modified_value = base_value + base_value*total_modifier
>> 다만 추가 생산 모디파이어는 생산 속도에 곱연산으로 반영됩니다. 
>> 
>>팩토리오의 생산량 증가는 base_speed*extra_modifier 속도로 진행되는 별도의 추가생산 과정을 통해 이루어지기 때문에 실질적으로 1회당 생산속도가 줄어드는 것으로 간주할수 있습니다. 
>>      
>>      extra_product_rate = extra_modifier +1
>>      modified_speed = base_speed*(extra_product_rate)

<h2>dependency_tracker.py</h2>
>레시피의 ingredients와 results를 바탕으로 의존성 트리를 생성합니다.
>
><h3>DependencyTracker</h3>
일반적인 레시피의 의존성 트리를 생성합니다.
>
>><h4>get_initial_recipe_req_dict()</h4>
>>두 개의 큐와 while문을 바탕으로 의존성 트리를 생성합니다.
>> - **total_recipe_needed_dict: dict**
>> 
>>   반환할 정보로, 딕셔너리입니다.
>>
>>   **find_recipe()** 메소드가 처리하지 못하는 일부 레시피를 제외한 대부분의 레시피 요구정보를 포함합니다.
> 
>   
>> - **obj_search_queue: list**
> 
>>   레시피 객체를 순회합니다. 
> 
>>   레시피 객체의 **ingredients**를 확인하여 **item_needed_queue**에 추가합니다.
>   
>>   **ingredients**는 딕셔너리 형태이며, **키**는 아이템의 이름, **값**은 필요한 아이템 수량을 의미합니다. 모든 키와 값을 **[키,값]** 형태의 리스트로 **item_needed_queue**에 추가합니다.
> 
>   
>> - **item_needed_queue: list**
>   
>>   **obj_search_queue**에서 받은 **[키,값]** 형태의 리스트를 처리합니다.
> 
>>   **find_recipe()** 메소드에 **[키,값]** 을 전달하여 필요한 레시피와 아이템 1개당 레시피 요구량을 **[recipe_name, amount]** 형태의 리스트로 돌려받습니다.
>   
>>       -1이 반환될 경우 cannot_process_item_dict 에 [키,값] 형태의 리스트를 변환, 저장합니다.
> 
>>    이렇게 전달받은 리스트는 두 가지 용도로 쓰입니다.
>>  1. 반환할 값인 **total_recipe_needed_dict**에 추가됩니다.
>>  2. 레시피 객체를 생성합니다. 레시피 객체에 **amount** 값을 attribute로 붙여준 후, 이 객체를 **obj_search_queue** 에 추가합니다. 
>>   
>> 
>>      obj_search_queue 를 순회하는 중엔 ingredients를 item_needed_queue에 추가하고,
>>      item_needed_queue 를 순회하는 중엔 레시피 객체를 obj_search_queue에 추가하게 됩니다.
>>      의존성(ingredients)을 가지지 않는 레시피, 즉 최하위 레시피가 나올 때 까지 반복합니다.
>
>><h4>find_recipe()</h4>
>>**[아이템, 수량]** 을 인자로 전달받아 어느 레시피가 얼마나 필요한지 반환합니다.
>> 
>> 일부 레시피는 레시피와 생산되는 아이템의 이름이 다르거나, 한 가지의 레시피에서 여러가지 결과물이 나옵니다. 이 경우 -1을 반환합니다.
> 
><h3>DependencyDictMerged</h3>
**cannot_process_item_dict** 를 별도의 로직으로 처리한 후, **DependencyTracker** 객체의 **total_recipe_dict**, **total_item_dict**와 합칩니다. 
>
>일단 구현해놓고 보자고 하드코딩을 해놓은 부분이 있는데, 추후 정리할 예정입니다.

<h2>oil_processing.py</h2>
>석유 가공 아이템을 처리합니다. 
>
>advanced-oil-processing 레시피를 통해 원유를 가공하면 중유, 경유, 석유가스의 세 가지 결과물이 나옵니다. 중유와 경유는 열분해 레시피를 통해 각각 경유와 석유가스로 변환이 가능합니다.
>
>현재 구현된 것은 원유를 최소한으로 사용하면서(즉 advanced-oil-processing을 최소한으로 줄이면서) 요구조건을 충족시키는 비율으로, 추후 열분해 옵션을 끄고 켤 수 있도록 할 예정이며, 석탄 액화도 옵션으로 넣을 예정입니다.
>
>열분해 비율을 구하는 방법은 이렇습니다.
>
>> 1. advanced-oil-processing(**이하 adv**)의 산출물은 **중유 25, 경유 45, 석유가스 55**
>> 2. 중유는 열분해로 얻을 수 없으니 (중유 필요량/25) 만큼의 **adv**가 필요합니다. 이를 변수 **a**에 저장합니다. 리스트 **extra**에는 **adv**를 통해 생산된 잉여 자원의 수량을 저장합니다.
>> 3. 경유는 중유를 열분해해서 구할 수 있습니다.
>>   1. 2번 과정을 거치며 이미 생산된 경유의 총량은 45***a** 입니다.
>>   2. 45***a** 보다 필요량이 많을 경우 **adv**를 더 생산해야합니다.
>>       1. 중유는 (3 / 4)에 생산량 모디파이어를 곱한 비율(변수 **h2l**)로 경유로 전환됩니다.
>>       2. 경유 요구량을 충족하는데 필요한 **adv**는 (경유 필요량/(45+25***h2l**)) 입니다. 이를 변수 **b**에 저장합니다. 
>> 4. 위를 반복하여 석유가스 요구량을 충족하는데 필요한 **adv**까지 구할 수 있습니다. (변수 **c**)
>> 5. **a+b+c**=총 adv 요구량
