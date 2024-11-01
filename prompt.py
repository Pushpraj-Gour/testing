prompt_adapt_for_new_brand = {
    "user_message": """\
You are tasked with adapting an existing prompt designed for the brand "Kurlon" and its product "Kurlon mattresses" to make it relevant for a different brand and product.

Here is the original prompt:
<original_prompt>
{original_prompt}
</original_prompt>

Adapt this prompt for the new brand "{new_brand}" and product "{new_product}". Follow these steps closely to ensure all brand-specific details are accurately revised:

1. Replace Brand Mentions: Substitute all instances of "Kurlon" and "Kurlon mattresses" with "{new_brand}" and "{new_product}" as appropriate.

2. Adapt Product-Specific Details: Modify any product-related descriptions specific to Kurlon mattresses to match the features, benefits, and target audience of "{new_product}". This includes:
   - Updating mentions of product features, materials, or attributes to reflect {new_product}'s unique selling points.
   - Revising descriptions of customer experiences, needs, or pain points to align with {new_product}'s market and customer base.
   - Ensuring that any references to product positioning or competitive comparisons are relevant to {new_brand} and {new_product}.

3. Preserve Original Prompt Structure and Objective: Maintain the primary structure, purpose, and instructions of the original prompt. The adaptation should:
   - Keep sections, question formats, and instructional steps intact.
   - Replace only those details necessary for making the prompt specific to {new_brand} and {new_product} while retaining the original focus on understanding customer insights, product perceptions, or other research objectives.

4. Adapt Tone and Language: Ensure the tone and style match the identity and target audience of "{new_brand}". If "{new_brand}" has a more formal or casual style than Kurlon, reflect this in the revised prompt.

5. Retain Dynamic Placeholders: Keep placeholders like `{transcript}`, `{questions}`, `{analysis}`, or any other placeholders that exist in the original prompt.

6. Preserve Original Metadata or API Schema: Automatically detect and carry over all metadata or API schema from the original prompt exactly as it appears. This includes all properties under `func_name`, `func_desc`, and `func_schema` without any alterations.

7. Final Review: Confirm that:
   - All instances of "Kurlon" and "Kurlon mattresses" are replaced with "{new_brand}" and "{new_product}".
   - Any examples, instructions, or references align with the context of {new_brand} and {new_product}.

Present the fully adapted prompt, including the unaltered metadata, within <revised_prompt> tags"""}