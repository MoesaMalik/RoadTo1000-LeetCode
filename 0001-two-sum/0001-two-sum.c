/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int* result = NULL;
    
    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) { // Avoid using the same index
            if (nums[i] + nums[j] == target) {
                result = (int*)malloc(2 * sizeof(int));
                if (result == NULL) {
                    *returnSize = 0;
                    return NULL; // Failed to allocate memory
                }
                result[0] = i;
                result[1] = j;
                *returnSize = 2;
                return result;
            }
        }
    }
    
    *returnSize = 0; // No solution found
    return NULL;
}